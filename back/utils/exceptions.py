"""Collection of reusable generic HTTP error Exception wrappers."""


class APIException(Exception):
    """Base for all standardised API exceptions."""

    def __init__(self, _desc: str, _code: int, _message: str, *args: object) -> None:
        super().__init__(*args)
        self.desc = _desc
        self.code = _code
        self.message = _message

    def __repr__(self) -> str:
        return self.message


class NeedsLogin(APIException):
    """Indicates a user's auth has expired."""

    def __init__(
        self,
        message: str = 'Authentication has expired, please log in again.',
        *args: object,
    ) -> None:
        super().__init__('NOT_LOGGED_IN', 401, message, *args)


class NeedsAuthorisation(APIException):
    """Indicates a user's auth does not allow access to a recourse."""

    def __init__(
        self,
        message: str = 'You do not have sufficient privileges to access this resource.',
        *args: object,
    ) -> None:
        super().__init__('UNPRIVILEGED', 403, message, *args)


class NotFound(APIException):
    """Indicates a resource does not exist."""

    def __init__(
        self,
        message: str = 'The requested resource could not be found.',
        *args: object,
    ) -> None:
        super().__init__('NOT_FOUND', 404, message, *args)


class ServerError(APIException):
    """Indicates an unidentified server error."""

    def __init__(
        self,
        message: str = 'Something went wrong processing your request.',
        *args: object,
    ) -> None:
        super().__init__('SERVER_ERROR', 500, message, *args)
