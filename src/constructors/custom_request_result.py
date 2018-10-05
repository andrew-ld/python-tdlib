from tdwrapper.factory import Method, Type


class customRequestResult(Type):
    #  the result of a custom request @result A JSON-serialized

    result = None  # type: "string"


class sendCustomRequest(Method):
    #  a custom request; for bots only @method The method
    #  @parameters JSON-serialized method parameters

    method = None  # type: "string"
    parameters = None  # type: "string"
