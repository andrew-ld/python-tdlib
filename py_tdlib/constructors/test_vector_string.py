from ..factory import Method, Type


class testVectorString(Type):
    #  simple object containing a vector of strings; for testing
    #  @value Vector of strings

    value = None  # type: "vector<string>"


class testCallVectorString(Method):
    #  testing only request. Returns the received vector of strings;
    #  testing only @x Vector of strings to return

    x = None  # type: "vector<string>"
