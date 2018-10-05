from tdwrapper.factory import Method, Type


class testInt(Type):
    #  simple object containing a number; for testing only @value

    value = None  # type: "int32"


class testSquareInt(Method):
    #  the squared received number; for testing only @x Number to square

    x = None  # type: "int32"
