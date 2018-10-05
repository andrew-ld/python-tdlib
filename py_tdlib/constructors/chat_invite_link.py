from ..factory import Method, Type


class chatInviteLink(Type):
    #  a chat invite link @invite_link Chat invite link

    invite_link = None  # type: "string"


class generateChatInviteLink(Method):
    #  a new invite link for a chat; the previously
    #  link is revoked. Available for basic groups, supergroups, and
    #  In basic groups this can be called only by
    #  group's creator; in supergroups and channels this requires appropriate
    #  rights @chat_id Chat identifier

    chat_id = None  # type: "int53"
