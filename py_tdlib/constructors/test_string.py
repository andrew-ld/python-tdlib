from ..factory import Method, Type


class testString(Type):
    # A simple object containing a string; for testing only, @value String

    value = None  # type: "string"


class testCallString(Method):
    # Returns the received string; for testing only, @x String to return

    x = None  # type: "string"
