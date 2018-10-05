from tdwrapper.factory import Method, Type


class testString(Type):
    #  simple object containing a string; for testing only @value

    value = None  # type: "string"


class testCallString(Method):
    #  the received string; for testing only @x String to

    x = None  # type: "string"
