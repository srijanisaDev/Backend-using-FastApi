class BooklyException(Exception):
    """This is the base class for all bookly errors."""
    pass


class InvalidToken(BooklyException):
    """User has provided an invalid token."""
    pass


class RevokedToken(BooklyException):
    """User has provided a token that has been revoked."""
    pass


class AccessTokenRequired(BooklyException):
    """User has provided a refresh token when an access token is needed."""
    pass


class RefreshTokenRequired(BooklyException):
    """User has provided an access token when a refresh token is needed."""
    pass


class UserAlreadyExists(BooklyException):
    """User has provided an email for a user who exists during sign up ."""
    pass


class InsufficientPermission(BooklyException):
    """User does not have the necessary permissions to perform an action."""
    pass


class BokNotFound(BooklyException):
    """Book not found."""
    pass