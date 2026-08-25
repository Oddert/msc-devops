"""Collection of standard response formatters to enforce consistency across all endpoints and enable cleaner code."""

from fastapi import Response, status as http_statuses


def respond_ok(
    response: Response | None = None,
    message: str = 'Request processed successfully.',
    status: int = 200,
    error: str | None = None,
    **kwargs,
):
    """Handless 200 code "OK" responses."""
    if response:
        response.status_code = http_statuses.HTTP_200_OK
    return {
        'status': status,
        'message': message,
        'error': error,
        **kwargs,
    }


def respond_created(
    response: Response | None = None,
    message: str = 'Request processed successfully.',
    status: int = 201,
    error: str | None = None,
    **kwargs,
):
    """Handless 201 code "Created" responses."""
    if response:
        response.status_code = http_statuses.HTTP_201_CREATED
    return {
        'status': status,
        'message': message,
        'error': error,
        **kwargs,
    }


def respond_bad_request(
    response: Response | None = None,
    message: str = 'The system was unable to process your request.',
    status: int = 400,
    error: str | None = 'Bad request.',
    **kwargs,
):
    """Handless generic 400-band responses."""
    if response:
        response.status_code = http_statuses.HTTP_400_BAD_REQUEST
    return {
        'status': status,
        'message': message,
        'error': error,
        **kwargs,
    }


def respond_unauthenticated(
    response: Response | None = None,
    message: str = 'You are not logged in. Please login and try again.',
    status: int = 401,
    error: str | None = 'Not authenticated.',
    **kwargs,
):
    """Handless 401 responses to indicate the user's auth has failed or expired."""
    if response:
        response.status_code = http_statuses.HTTP_401_UNAUTHORIZED
    return {
        'status': status,
        'message': message,
        'error': error,
        **kwargs,
    }


def respond_unauthorised(
    response: Response | None = None,
    message: str = 'You do not have sufficient privileges to access this resource.',
    status: int = 403,
    error: str | None = 'Unprivileged.',
    **kwargs,
):
    """Handless 403 responses to indicate the user's auth is insufficient."""
    if response:
        response.status_code = http_statuses.HTTP_403_FORBIDDEN
    return {
        'status': status,
        'message': message,
        'error': error,
        **kwargs,
    }


def respond_not_found(
    response: Response | None = None,
    message: str = 'The requested resource could not be found. Please check the request and try again.',
    status: int = 404,
    error: str | None = 'Not found.',
    **kwargs,
):
    """Handless 404 "Not found" responses."""
    if response:
        response.status_code = http_statuses.HTTP_404_NOT_FOUND
    return {
        'status': status,
        'message': message,
        'error': error,
        **kwargs,
    }


def respond_server_error(
    response: Response | None = None,
    message: str = 'Something went wrong processing your request.',
    status: int = 500,
    error: str | None = 'Unknown server error.',
    **kwargs,
):
    """Handless generic 500 band responses for non-elaborated server errors."""
    if response:
        response.status_code = http_statuses.HTTP_500_INTERNAL_SERVER_ERROR
    return {
        'status': status,
        'message': message,
        'error': error,
        **kwargs,
    }
