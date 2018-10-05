from tdwrapper.factory import Method, Type


class testVectorInt(Type):
    #  simple object containing a vector of numbers; for testing
    #  @value Vector of numbers

    value = None  # type: "vector<int32>"


class testCallVectorInt(Method):
    #  the received vector of numbers; for testing only @x
    #  of numbers to return

    x = None  # type: "vector<int32>"
