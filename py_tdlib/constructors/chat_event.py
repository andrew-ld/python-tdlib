from ..factory import Type


class chatEvent(Type):
    # Represents a chat event, @id Chat event identifier, @date Point
    # in time (Unix timestamp) when the event happened, @user_id Identifier
    # of the user who performed the action that triggered the
    # event, @action Action performed by the user

    id = None  # type: "int64"
    date = None  # type: "int32"
    user_id = None  # type: "int32"
    action = None  # type: "ChatEventAction"
