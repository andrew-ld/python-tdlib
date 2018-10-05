from ..factory import Method, Type


class testVectorString(Type):
    # A simple object containing a vector of strings; for testing
    # only @value Vector of strings

    value = None  # type: "vector<string>"


class testCallVectorString(Method):
    # For testing only request. Returns the received vector of strings;
    # for testing only @x Vector of strings to return

    x = None  # type: "vector<string>"
