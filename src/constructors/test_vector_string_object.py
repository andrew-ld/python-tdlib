from tdwrapper.factory import Method, Type


class testVectorStringObject(Type):
    #  simple object containing a vector of objects that hold
    #  string; for testing only @value Vector of objects

    value = None  # type: "vector<testString>"


class testCallVectorStringObject(Method):
    #  the received vector of objects containing a string; for
    #  only @x Vector of objects to return

    x = None  # type: "vector<testString>"
