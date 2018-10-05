from ..factory import Type


class chatEventMessageEdited(Type):
    # A message was edited, @old_message The original message before the
    # edit, @new_message The message after it was edited

    old_message = None  # type: "message"
    new_message = None  # type: "message"


class chatEventMessageDeleted(Type):
    # A message was deleted, @message Deleted message

    message = None  # type: "message"


class chatEventMessagePinned(Type):
    # A message was pinned, @message Pinned message

    message = None  # type: "message"


class chatEventMessageUnpinned(Type):
    # A message was unpinned

    pass


class chatEventMemberJoined(Type):
    # A new member joined the chat

    pass


class chatEventMemberLeft(Type):
    # A member left the chat

    pass


class chatEventMemberInvited(Type):
    # A new chat member was invited, @user_id New member user
    # identifier, @status New member status

    user_id = None  # type: "int32"
    status = None  # type: "ChatMemberStatus"


class chatEventMemberPromoted(Type):
    # A chat member has gained/lost administrator status, or the list
    # of their administrator privileges has changed, @user_id Chat member user
    # identifier, @old_status Previous status of the chat member, @new_status New
    # status of the chat member

    user_id = None  # type: "int32"
    old_status = None  # type: "ChatMemberStatus"
    new_status = None  # type: "ChatMemberStatus"


class chatEventMemberRestricted(Type):
    # A chat member was restricted/unrestricted or banned/unbanned, or the list
    # of their restrictions has changed, @user_id Chat member user identifier
    # @old_status Previous status of the chat member, @new_status New status
    # of the chat member

    user_id = None  # type: "int32"
    old_status = None  # type: "ChatMemberStatus"
    new_status = None  # type: "ChatMemberStatus"


class chatEventTitleChanged(Type):
    # The chat title was changed, @old_title Previous chat title, @new_title New chat title

    old_title = None  # type: "string"
    new_title = None  # type: "string"


class chatEventDescriptionChanged(Type):
    # The chat description was changed, @old_description Previous chat description, @new_description New chat description

    old_description = None  # type: "string"
    new_description = None  # type: "string"


class chatEventUsernameChanged(Type):
    # The chat username was changed, @old_username Previous chat username, @new_username New chat username

    old_username = None  # type: "string"
    new_username = None  # type: "string"


class chatEventPhotoChanged(Type):
    # The chat photo was changed, @old_photo Previous chat photo value;
    # may be null, @new_photo New chat photo value; may be null

    old_photo = None  # type: "chatPhoto"
    new_photo = None  # type: "chatPhoto"


class chatEventInvitesToggled(Type):
    # The anyone_can_invite setting of a supergroup chat was toggled, @anyone_can_invite
    # New value of anyone_can_invite

    anyone_can_invite = None  # type: "Bool"


class chatEventSignMessagesToggled(Type):
    # The sign_messages setting of a channel was toggled, @sign_messages New value of sign_messages

    sign_messages = None  # type: "Bool"


class chatEventStickerSetChanged(Type):
    # The supergroup sticker set was changed, @old_sticker_set_id Previous identifier of
    # the chat sticker set; 0 if none, @new_sticker_set_id New identifier
    # of the chat sticker set; 0 if none

    old_sticker_set_id = None  # type: "int64"
    new_sticker_set_id = None  # type: "int64"


class chatEventIsAllHistoryAvailableToggled(Type):
    # The is_all_history_available setting of a supergroup was toggled, @is_all_history_available New value of is_all_history_available

    is_all_history_available = None  # type: "Bool"
