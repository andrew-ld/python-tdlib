from ..factory import Method, Type


class chatInviteLinkInfo(Type):
    # Contains information about a chat invite link

    chat_id = None  # type: "int53"
    type = None  # type: "ChatType"
    title = None  # type: "string"
    photo = None  # type: "chatPhoto"
    member_count = None  # type: "int32"
    member_user_ids = None  # type: "vector<int32>"
    is_public = None  # type: "Bool"


class checkChatInviteLink(Method):
    # Checks the validity of an invite link for a chat
    # and returns information about the corresponding chat @invite_link Invite link
    # to be checked; should begin with "https://t.me/joinchat/", "https://telegram.me/joinchat/", or "https://telegram.dog/joinchat/"

    invite_link = None  # type: "string"
