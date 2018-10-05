from ..factory import Method, Type


class error(Type):
    #  object of this type can be returned on every
    #  call, in case of an error

    code = None  # type: "int32"
    message = None  # type: "string"


class testUseError(Method):
    #  nothing and ensures that the Error object is used; for testing only

    pass
