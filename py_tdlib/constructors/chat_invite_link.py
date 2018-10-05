from ..factory import Method, Type


class chatInviteLink(Type):
    # Contains a chat invite link @invite_link Chat invite link

    invite_link = None  # type: "string"


class generateChatInviteLink(Method):
    # Generates a new invite link for a chat; the previously
    # generated link is revoked. Available for basic groups, supergroups, and
    # channels. In basic groups this can be called only by
    # the group's creator; in supergroups and channels this requires appropriate
    # administrator rights @chat_id Chat identifier

    chat_id = None  # type: "int53"
