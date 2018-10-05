from ..factory import Method, Type


class customRequestResult(Type):
    # Contains the result of a custom request @result A JSON-serialized result

    result = None  # type: "string"


class sendCustomRequest(Method):
    # Sends a custom request; for bots only @method The method
    # name @parameters JSON-serialized method parameters

    method = None  # type: "string"
    parameters = None  # type: "string"
