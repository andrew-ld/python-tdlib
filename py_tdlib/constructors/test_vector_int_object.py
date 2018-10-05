from ..factory import Method, Type


class testVectorIntObject(Type):
    #  simple object containing a vector of objects that hold
    #  number; for testing only @value Vector of objects

    value = None  # type: "vector<testInt>"


class testCallVectorIntObject(Method):
    #  the received vector of objects containing a number; for
    #  only @x Vector of objects to return

    x = None  # type: "vector<testInt>"
