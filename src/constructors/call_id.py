from ..factory import Method, Type


class callId(Type):
    #  the call identifier @id Call identifier

    id = None  # type: "int32"


class createCall(Method):
    #  a new call @user_id Identifier of the user to
    #  called @protocol Description of the call protocols supported by the client

    user_id = None  # type: "int32"
    protocol = None  # type: "callProtocol"
