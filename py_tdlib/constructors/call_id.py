from ..factory import Method, Type


class callId(Type):
    # Contains the call identifier @id Call identifier

    id = None  # type: "int32"


class createCall(Method):
    # Creates a new call @user_id Identifier of the user to
    # be called @protocol Description of the call protocols supported by the client

    user_id = None  # type: "int32"
    protocol = None  # type: "callProtocol"
