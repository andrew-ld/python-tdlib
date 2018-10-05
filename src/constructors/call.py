from tdwrapper.factory import Type


class call(Type):
    #  a call @id Call identifier, not persistent @user_id Peer
    #  identifier @is_outgoing True, if the call is outgoing @state Call state

    id = None  # type: "int32"
    user_id = None  # type: "int32"
    is_outgoing = None  # type: "Bool"
    state = None  # type: "CallState"
