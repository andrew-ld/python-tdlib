from ..factory import Method, Type


class testVectorStringObject(Type):
    # A simple object containing a vector of objects that hold
    # a string; for testing only, @value Vector of objects

    value = None  # type: "vector<testString>"


class testCallVectorStringObject(Method):
    # Returns the received vector of objects containing a string; for
    # testing only, @x Vector of objects to return

    x = None  # type: "vector<testString>"
