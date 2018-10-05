from tdwrapper.factory import Type


class chatEventMessageEdited(Type):
    #  message was edited @old_message The original message before the
    #  @new_message The message after it was edited

    old_message = None  # type: "message"
    new_message = None  # type: "message"


class chatEventMessageDeleted(Type):
    #  message was deleted @message Deleted message

    message = None  # type: "message"


class chatEventMessagePinned(Type):
    #  message was pinned @message Pinned message

    message = None  # type: "message"


class chatEventMessageUnpinned(Type):
    #  message was unpinned

    pass


class chatEventMemberJoined(Type):
    #  new member joined the chat

    pass


class chatEventMemberLeft(Type):
    #  member left the chat

    pass


class chatEventMemberInvited(Type):
    #  new chat member was invited @user_id New member user
    #  @status New member status

    user_id = None  # type: "int32"
    status = None  # type: "ChatMemberStatus"


class chatEventMemberPromoted(Type):
    #  chat member has gained/lost administrator status, or the list
    #  their administrator privileges has changed @user_id Chat member user
    #  @old_status Previous status of the chat member @new_status New
    #  of the chat member

    user_id = None  # type: "int32"
    old_status = None  # type: "ChatMemberStatus"
    new_status = None  # type: "ChatMemberStatus"


class chatEventMemberRestricted(Type):
    #  chat member was restricted/unrestricted or banned/unbanned, or the list
    #  their restrictions has changed @user_id Chat member user identifier
    #  Previous status of the chat member @new_status New status
    #  the chat member

    user_id = None  # type: "int32"
    old_status = None  # type: "ChatMemberStatus"
    new_status = None  # type: "ChatMemberStatus"


class chatEventTitleChanged(Type):
    #  chat title was changed @old_title Previous chat title @new_title New chat title

    old_title = None  # type: "string"
    new_title = None  # type: "string"


class chatEventDescriptionChanged(Type):
    #  chat description was changed @old_description Previous chat description @new_description New chat description

    old_description = None  # type: "string"
    new_description = None  # type: "string"


class chatEventUsernameChanged(Type):
    #  chat username was changed @old_username Previous chat username @new_username New chat username

    old_username = None  # type: "string"
    new_username = None  # type: "string"


class chatEventPhotoChanged(Type):
    #  chat photo was changed @old_photo Previous chat photo value;
    #  be null @new_photo New chat photo value; may be

    old_photo = None  # type: "chatPhoto"
    new_photo = None  # type: "chatPhoto"


class chatEventInvitesToggled(Type):
    #  anyone_can_invite setting of a supergroup chat was toggled @anyone_can_invite
    #  value of anyone_can_invite

    anyone_can_invite = None  # type: "Bool"


class chatEventSignMessagesToggled(Type):
    #  sign_messages setting of a channel was toggled @sign_messages New value of sign_messages

    sign_messages = None  # type: "Bool"


class chatEventStickerSetChanged(Type):
    #  supergroup sticker set was changed @old_sticker_set_id Previous identifier of
    #  chat sticker set; 0 if none @new_sticker_set_id New identifier
    #  the chat sticker set; 0 if none

    old_sticker_set_id = None  # type: "int64"
    new_sticker_set_id = None  # type: "int64"


class chatEventIsAllHistoryAvailableToggled(Type):
    #  is_all_history_available setting of a supergroup was toggled @is_all_history_available New value of is_all_history_available

    is_all_history_available = None  # type: "Bool"
