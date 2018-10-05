from ..factory import Method, Type


class testVectorIntObject(Type):
    # A simple object containing a vector of objects that hold
    # a number; for testing only @value Vector of objects

    value = None  # type: "vector<testInt>"


class testCallVectorIntObject(Method):
    # Returns the received vector of objects containing a number; for
    # testing only @x Vector of objects to return

    x = None  # type: "vector<testInt>"
