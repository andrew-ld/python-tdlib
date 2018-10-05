from ..factory import Type


class chatMemberStatusCreator(Type):
    # The user is the creator of a chat and has
    # all the administrator privileges, @is_member True, if the user is
    # a member of the chat

    is_member = None  # type: "Bool"


class chatMemberStatusAdministrator(Type):
    # The user is a member of a chat and has
    # some additional privileges. In basic groups, administrators can edit and
    # delete messages sent by others, add new members, and ban
    # unprivileged members. In supergroups and channels, there are more detailed
    # options for administrator privileges

    can_be_edited = None  # type: "Bool"
    can_change_info = None  # type: "Bool"
    can_post_messages = None  # type: "Bool"
    can_edit_messages = None  # type: "Bool"
    can_delete_messages = None  # type: "Bool"
    can_invite_users = None  # type: "Bool"
    can_restrict_members = None  # type: "Bool"
    can_pin_messages = None  # type: "Bool"
    can_promote_members = None  # type: "Bool"


class chatMemberStatusMember(Type):
    # The user is a member of a chat, without any
    # additional privileges or restrictions

    pass


class chatMemberStatusRestricted(Type):
    # The user is under certain restrictions in the chat. Not
    # supported in basic groups and channels

    is_member = None  # type: "Bool"
    restricted_until_date = None  # type: "int32"
    can_send_messages = None  # type: "Bool"
    can_send_media_messages = None  # type: "Bool"
    can_send_other_messages = None  # type: "Bool"
    can_add_web_page_previews = None  # type: "Bool"


class chatMemberStatusLeft(Type):
    # The user is not a chat member

    pass


class chatMemberStatusBanned(Type):
    # The user was banned (and hence is not a member
    # of the chat). Implies the user can't return to the
    # chat or view messages

    banned_until_date = None  # type: "int32"
