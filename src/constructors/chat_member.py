from tdwrapper.factory import Method, Type


class chatMember(Type):
    #  user with information about joining/leaving a chat @user_id User
    #  of the chat member @inviter_user_id Identifier of a user
    #  invited/promoted/banned this member in the chat; 0 if unknown

    user_id = None  # type: "int32"
    inviter_user_id = None  # type: "int32"
    joined_chat_date = None  # type: "int32"
    status = None  # type: "ChatMemberStatus"
    bot_info = None  # type: "botInfo"


class getChatMember(Method):
    #  information about a single member of a chat @chat_id
    #  identifier @user_id User identifier

    chat_id = None  # type: "int53"
    user_id = None  # type: "int32"
