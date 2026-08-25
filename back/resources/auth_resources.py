"""Handles all responses on the base endpoint "/"."""

from datetime import datetime

from fastapi import APIRouter, Depends, Request, Response
from sqlalchemy.orm import Session

from config.database import get_db

from models.instance_model import InstanceModel
from models.token_exclude_model import TokenExcludeModel
from models.user_model import UserModel
from models.watchlist_model import WatchlistModel

from schemas.auth_schemas import PostLogin, PostSignup, PostTokenRefresh

from security.hash import get_hashed_pwd, verify_hashed_pwd
from security.roles import get_org_ids_for_user, validate_role_list
from security.token import create_auth_tokens, validate_refresh_jwt

from utils.exceptions import NeedsLogin, NotFound
from utils.responses import (
    respond_bad_request,
    respond_not_found,
    respond_ok,
    respond_server_error,
    respond_unauthenticated,
)

router = APIRouter(prefix='/auth')


@router.post('/signup')
def create_user(
    request: Request,
    response: Response,
    user: PostSignup,
    database: Session = Depends(get_db),
):
    """Fallback endpoint for the root of the API."""

    try:
        # IDEA: Potentially add additional final password validation.
        retrieved_user = UserModel.find_by_username(user.username, database)

        if retrieved_user:
            return respond_bad_request(
                response, message='A user with that username already exists.'
            )

        role_check_result = validate_role_list(user.areas)
        roles_joined = ','.join(user.areas)

        if not role_check_result.success:
            return respond_bad_request(
                response,
                f'One of more requested roles is not valid. Please check the following roles: "{roles_joined}"',
            )

        created_user = UserModel(
            areas=roles_joined,
            password=get_hashed_pwd(user.password),
            readable_name=user.readableName if user.readableName else user.username,
            username=user.username,
        )

        database.add(created_user)
        database.commit()
        database.flush()

        default_watchlist = WatchlistModel(
            description='',
            racf=user.username,
            title='Default watchlist',
        )

        database.add(default_watchlist)

        org_ids = get_org_ids_for_user(user.areas)
        instances = InstanceModel.find_by_org_id_list(org_ids, user.username, database)

        default_watchlist.instances = instances

        database.commit()
        database.flush()

        access_token, refresh_token = create_auth_tokens(created_user)

        return respond_ok(
            response,
            accessToken=access_token,
            refreshToken=refresh_token,
            user=created_user.to_json(),
            defaultWatchlist=default_watchlist.to_json(),
        )
    except Exception as ex:
        return respond_server_error(response, error=str(ex))


@router.post('/login')
def login_user(
    request: Request,
    response: Response,
    user: PostLogin,
    database: Session = Depends(get_db),
):
    """Fallback endpoint for the root of the API."""

    try:
        retrieved_user = UserModel.find_by_username(user.username, database)

        if not retrieved_user:
            return respond_bad_request(
                response, message='No user by that username exists.'
            )

        if not verify_hashed_pwd(
            user.password, bytes(retrieved_user.password, 'utf-8')
        ):
            return respond_unauthenticated(
                response, message='Incorrect username or password.'
            )

        access_token, refresh_token = create_auth_tokens(retrieved_user)

        return respond_ok(
            response, accessToken=access_token, refreshToken=refresh_token
        )
    except Exception as ex:
        return respond_server_error(response, error=str(ex))


@router.post('/token-refresh')
def token_refresh(
    request: Request,
    response: Response,
    token_request: PostTokenRefresh,
    database: Session = Depends(get_db),
):
    """
    Re-authenticates a user using their one-time use refresh token.
    Adds the refresh token to the exclude list and provides a new Access and Refresh token pair.
    """

    try:
        token_verify_result = validate_refresh_jwt(token_request.refreshToken)

        if not token_verify_result.success:
            raise NeedsLogin(
                token_verify_result.error
                if token_verify_result.error
                else 'Token decode failed.'
            )

        token = token_verify_result.payload

        retrieved_te_record = TokenExcludeModel.find_by_jti(token['jti'], database)

        if retrieved_te_record:
            raise NeedsLogin('Refresh token has already been used.')

        retrieved_user = UserModel.find_by_username(token['sub'], database)

        if not retrieved_user:
            raise NotFound('No user by that username exists.')

        created_te_record = TokenExcludeModel(
            expires=datetime.fromtimestamp(token['exp']),
            jti=token['jti'],
        )

        database.add(created_te_record)
        database.commit()

        access_token, refresh_token = create_auth_tokens(retrieved_user)

        return respond_ok(
            response, accessToken=access_token, refreshToken=refresh_token
        )
    except NotFound as ex:
        return respond_not_found(response, ex.message)
    except NeedsLogin as ex:
        return respond_unauthenticated(response, ex.message)
    except Exception as ex:
        return respond_server_error(response, error=str(ex))
