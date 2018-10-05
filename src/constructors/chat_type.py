from tdwrapper.factory import Type


class chatTypePrivate(Type):
    #  ordinary chat with a user @user_id User identifier

    user_id = None  # type: "int32"


class chatTypeBasicGroup(Type):
    #  basic group (i.e., a chat with 0-200 other users)
    #  Basic group identifier

    basic_group_id = None  # type: "int32"


class chatTypeSupergroup(Type):
    #  supergroup (i.e. a chat with up to GetOption("supergroup_max_size") other
    #  or channel (with unlimited members) @supergroup_id Supergroup or channel
    #  @is_channel True, if the supergroup is a channel

    supergroup_id = None  # type: "int32"
    is_channel = None  # type: "Bool"


class chatTypeSecret(Type):
    #  secret chat with a user @secret_chat_id Secret chat identifier
    #  User identifier of the secret chat peer

    secret_chat_id = None  # type: "int32"
    user_id = None  # type: "int32"
