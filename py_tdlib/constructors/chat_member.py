from ..factory import Method, Type


class chatMember(Type):
    # A user with information about joining/leaving a chat, @user_id User
    # identifier of the chat member, @inviter_user_id Identifier of a user
    # that invited/promoted/banned this member in the chat; 0 if unknown

    user_id = None  # type: "int32"
    inviter_user_id = None  # type: "int32"
    joined_chat_date = None  # type: "int32"
    status = None  # type: "ChatMemberStatus"
    bot_info = None  # type: "botInfo"


class getChatMember(Method):
    # Returns information about a single member of a chat, @chat_id
    # Chat identifier, @user_id User identifier

    chat_id = None  # type: "int53"
    user_id = None  # type: "int32"
