from ..factory import Method, Type


class temporaryPasswordState(Type):
    # Returns information about the availability of a temporary password, which
    # can be used for payments @has_password True, if a temporary
    # password is available @valid_for Time left before the temporary password expires, in seconds

    has_password = None  # type: "Bool"
    valid_for = None  # type: "int32"


class createTemporaryPassword(Method):
    # Creates a new temporary password for processing payments @password Persistent
    # user password @valid_for Time during which the temporary password will
    # be valid, in seconds; should be between 60 and 86400

    password = None  # type: "string"
    valid_for = None  # type: "int32"


class getTemporaryPasswordState(Method):
    # Returns information about the current temporary password

    pass
