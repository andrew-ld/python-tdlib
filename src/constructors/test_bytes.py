from ..factory import Method, Type


class testBytes(Type):
    #  simple object containing a sequence of bytes; for testing only @value Bytes

    value = None  # type: "bytes"


class testCallBytes(Method):
    #  the received bytes; for testing only @x Bytes to

    x = None  # type: "bytes"
