from ..factory import Method, Type


class checkChatUsernameResultOk(Type):
    #  username can be set

    pass


class checkChatUsernameResultUsernameInvalid(Type):
    #  username is invalid

    pass


class checkChatUsernameResultUsernameOccupied(Type):
    #  username is occupied

    pass


class checkChatUsernameResultPublicChatsTooMuch(Type):
    #  user has too much public chats, one of them
    #  be made private first

    pass


class checkChatUsernameResultPublicGroupsUnavailable(Type):
    #  user can't be a member of a public supergroup

    pass


class checkChatUsername(Method):
    #  whether a username can be set for a chat
    #  Chat identifier; should be identifier of a supergroup chat,
    #  a channel chat, or a private chat with self,
    #  zero if chat is being created @username Username to be checked

    chat_id = None  # type: "int64"
    username = None  # type: "string"
