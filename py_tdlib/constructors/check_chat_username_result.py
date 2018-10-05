from ..factory import Method, Type


class checkChatUsernameResultOk(Type):
    # The username can be set

    pass


class checkChatUsernameResultUsernameInvalid(Type):
    # The username is invalid

    pass


class checkChatUsernameResultUsernameOccupied(Type):
    # The username is occupied

    pass


class checkChatUsernameResultPublicChatsTooMuch(Type):
    # The user has too much public chats, one of them
    # should be made private first

    pass


class checkChatUsernameResultPublicGroupsUnavailable(Type):
    # The user can't be a member of a public supergroup

    pass


class checkChatUsername(Method):
    # Checks whether a username can be set for a chat
    # @chat_id Chat identifier; should be identifier of a supergroup chat,
    # or a channel chat, or a private chat with self,
    # or zero if chat is being created, @username Username to be checked

    chat_id = None  # type: "int64"
    username = None  # type: "string"
