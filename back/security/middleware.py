from functools import wraps
from typing import Annotated, List, Optional

from fastapi import (
    Query,
    Request,
    Response,
    status,
    WebSocket,
    WebSocketException,
)
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

from constants.auth_constants import role_lookup

from security.token import validate_access_jwt

from utils.exceptions import NeedsLogin, NeedsAuthorisation
from utils.responses import (
    respond_unauthenticated,
    respond_unauthorised,
    respond_server_error,
)


def verify_extracted_token(access_token: str, for_areas: Optional[List[str]] = None):
    """Performs the bulk of the logic required to decode and verify an incoming access token."""
    token_verify_result = validate_access_jwt(access_token)

    if not token_verify_result.success:
        raise NeedsLogin(
            token_verify_result.error
            if token_verify_result.error
            else 'Token decode failed.'
        )

    decoded_verified_token = token_verify_result.payload

    if 'roles' not in decoded_verified_token:
        raise NeedsLogin('Token format invalid.')

    access_granted = False

    for role in decoded_verified_token['roles']:
        if role in role_lookup:
            if for_areas:
                access_group = role_lookup[role]['access_codes']
                for required_area in for_areas:
                    if required_area in access_group:
                        access_granted = True
            else:
                access_granted = True

    if not access_granted:
        raise NeedsAuthorisation('Insufficient roles for requested resource.')

    return decoded_verified_token


def protected_endpoint(for_areas: Optional[List[str]] = None):
    """
    Middleware to protect resources from access by unauthenticated of unauthorised users.
    Passing a list of area codes to
    """

    def decorator(func):
        @wraps(func)
        async def decorated(request: Request, response: Response, *args, **kwargs):
            try:
                print(request.url)
                access_token = extract_access_token(request)

                decoded_verified_token = verify_extracted_token(access_token, for_areas)

                kwargs['racfid'] = decoded_verified_token['sub']
                kwargs['roles'] = decoded_verified_token['roles']

                return await func(request=request, response=response, *args, **kwargs)

            except NeedsLogin as ex:
                return respond_unauthenticated(
                    response=response, message=ex.message, error=ex.desc
                )
            except NeedsAuthorisation as ex:
                return respond_unauthorised(
                    response=response, message=ex.message, error=ex.desc
                )
            except Exception as ex:
                return respond_server_error(response=response, error=str(ex))

        return decorated

    return decorator


def extract_access_token(request: Request) -> str:
    """Extracts the authorisation header from an incoming request, validates the Bearer token format, and returns what is believed to be a valid token (pre-verification and decoding)."""
    auth = request.headers.get('Authorization', None)
    if not auth:
        raise NeedsLogin('No authorisation header found in request.')
    auth_segments = auth.split(' ')
    if not auth.lower().startswith('bearer ') or len(auth_segments) != 2:
        raise NeedsLogin('Header "Authorization" was not a valid Bearer token.')
    return auth_segments[1]


async def get_ws_token(
    websocket: WebSocket,
    token: Annotated[str | None, Query()] = None,
):
    """Dependency function to extract an auth token from a websocket connector."""
    if token is None:
        raise WebSocketException(code=status.WS_1008_POLICY_VIOLATION)
    return token


class CustomCorsMW(BaseHTTPMiddleware):
    '''Customised middleware to handle CORs. Allows us to inject specific Access Control headers to deal with rules which disallow "*"'''

    def __init__(self, app) -> None:
        super().__init__(app)

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        origin = request.headers.get('origin')

        if (
            request.method == 'OPTIONS'
            and 'access-control-request-method' in request.headers
        ):
            allow_headers = 'Authorization,Content-Type,Accept,Origin,X-Requested-With'
            headers = {
                'Access-Control-Allow-Origin': origin or '*',
                'Access-Control-Allow-Methods': 'GET,POST,PUT,DELETE,PATCH,OPTIONS',
                'Access-Control-Allow-Headers': allow_headers,
                'Access-Control-Allow-Credentials': 'true',
            }
            return JSONResponse(
                content={'detail': 'CORS pre-flight successful'}, headers=headers
            )

        response = await call_next(request)

        if origin is None:
            return response

        response.headers['Access-Control-Allow-Origin'] = origin
        response.headers['Access-Control-Allow-Credentials'] = 'true'

        return response
