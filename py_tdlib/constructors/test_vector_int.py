from ..factory import Method, Type


class testVectorInt(Type):
    # A simple object containing a vector of numbers; for testing
    # only, @value Vector of numbers

    value = None  # type: "vector<int32>"


class testCallVectorInt(Method):
    # Returns the received vector of numbers; for testing only, @x
    # Vector of numbers to return

    x = None  # type: "vector<int32>"
