from ..factory import Method, Type


class testInt(Type):
    # A simple object containing a number; for testing only, @value Number

    value = None  # type: "int32"


class testSquareInt(Method):
    # Returns the squared received number; for testing only, @x Number to square

    x = None  # type: "int32"
