"""Functions to create and validate user access tokens and refresh tokens."""

import jwt

from datetime import datetime, timedelta
from uuid import uuid4 as uuid
from typing import List, Any

from config.variables import JWT_ACCESS_SECRET, JWT_REFRESH_SECRET

from constants.auth_constants import jwt_alg

from models.user_model import UserModel


class JWTDecodeResult:
    def __init__(
        self,
        _error: str | None = None,
        _success: bool = False,
        _payload: Any = None,
    ) -> None:
        self.success = _success
        self.payload = _payload
        self.error = _error


def create_access_jwt(username: str, roles: List[str]):
    """Creates a user Access Token."""
    if not JWT_ACCESS_SECRET or not len(JWT_ACCESS_SECRET):
        raise ValueError(
            'Value for JWT_ACCESS_SECRET not supplied. Please check the application config.'
        )
    token_body = {
        'sub': username,
        'jti': str(uuid()),
        'roles': roles,
        'exp': datetime.now() + timedelta(hours=1),
    }
    return jwt.encode(token_body, JWT_ACCESS_SECRET, algorithm=jwt_alg)


def create_refresh_jwt(username: str):
    """Creates a user Refresh Token."""
    if not JWT_REFRESH_SECRET or not len(JWT_REFRESH_SECRET):
        raise ValueError(
            'Value for JWT_REFRESH_SECRET not supplied. Please check the application config.'
        )
    token_body = {
        'sub': username,
        'jti': str(uuid()),
        'exp': datetime.now() + timedelta(days=3),
    }
    return jwt.encode(token_body, JWT_REFRESH_SECRET, algorithm=jwt_alg)


def validate_and_decode_jwt(token: str, secret: str) -> JWTDecodeResult:
    """Validates a JWT for a given secret."""
    try:
        payload = jwt.decode(token, secret, algorithms=[jwt_alg])
        return JWTDecodeResult(None, True, payload)
    except jwt.ExpiredSignatureError:
        return JWTDecodeResult('Token has expired.')
    except jwt.InvalidTokenError:
        return JWTDecodeResult('Token is invalid.')
    except Exception as ex:
        return JWTDecodeResult(str(ex))


def validate_access_jwt(access_token: str) -> JWTDecodeResult:
    """Decodes and validates a user's access token."""
    if not JWT_ACCESS_SECRET or not len(JWT_ACCESS_SECRET):
        raise ValueError(
            'Value for JWT_ACCESS_SECRET not supplied. Please check the application config.'
        )
    return validate_and_decode_jwt(access_token, JWT_ACCESS_SECRET)


def validate_refresh_jwt(refresh_token: str) -> JWTDecodeResult:
    """Decodes and validates a user's refresh token."""
    if not JWT_REFRESH_SECRET or not len(JWT_REFRESH_SECRET):
        raise ValueError(
            'Value for JWT_REFRESH_SECRET not supplied. Please check the application config.'
        )
    return validate_and_decode_jwt(refresh_token, JWT_REFRESH_SECRET)


def create_auth_tokens(user: UserModel):
    """Creates an Access and Refresh token after successful user authentication."""
    access_token = create_access_jwt(
        user.username,
        user.get_roles_as_list(),
    )
    refresh_token = create_refresh_jwt(user.username)

    return access_token, refresh_token
