from ..factory import Method, Type


class error(Type):
    # An object of this type can be returned on every
    # function call, in case of an error

    code = None  # type: "int32"
    message = None  # type: "string"


class testUseError(Method):
    # Does nothing and ensures that the Error object is used; for testing only

    pass
