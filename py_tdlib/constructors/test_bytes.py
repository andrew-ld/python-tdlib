from ..factory import Method, Type


class testBytes(Type):
    # A simple object containing a sequence of bytes; for testing only @value Bytes

    value = None  # type: "bytes"


class testCallBytes(Method):
    # Returns the received bytes; for testing only @x Bytes to return

    x = None  # type: "bytes"
