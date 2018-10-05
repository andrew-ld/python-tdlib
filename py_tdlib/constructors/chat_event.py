from ..factory import Type


class chatEvent(Type):
    #  a chat event @id Chat event identifier @date Point
    #  time (Unix timestamp) when the event happened @user_id Identifier
    #  the user who performed the action that triggered the
    #  @action Action performed by the user

    id = None  # type: "int64"
    date = None  # type: "int32"
    user_id = None  # type: "int32"
    action = None  # type: "ChatEventAction"
