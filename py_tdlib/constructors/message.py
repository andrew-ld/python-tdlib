from ..factory import Method, Type


class message(Type):
    # Describes a message

    id = None  # type: "int53"
    sender_user_id = None  # type: "int32"
    chat_id = None  # type: "int53"
    sending_state = None  # type: "MessageSendingState"
    is_outgoing = None  # type: "Bool"
    can_be_edited = None  # type: "Bool"
    can_be_forwarded = None  # type: "Bool"
    can_be_deleted_only_for_self = None  # type: "Bool"
    can_be_deleted_for_all_users = None  # type: "Bool"
    is_channel_post = None  # type: "Bool"
    contains_unread_mention = None  # type: "Bool"
    date = None  # type: "int32"
    edit_date = None  # type: "int32"
    forward_info = None  # type: "MessageForwardInfo"
    reply_to_message_id = None  # type: "int53"
    ttl = None  # type: "int32"
    ttl_expires_in = None  # type: "double"
    via_bot_user_id = None  # type: "int32"
    author_signature = None  # type: "string"
    views = None  # type: "int32"
    media_album_id = None  # type: "int64"
    content = None  # type: "MessageContent"
    reply_markup = None  # type: "ReplyMarkup"


class getMessage(Method):
    # Returns information about a message, @chat_id Identifier of the chat
    # the message belongs to, @message_id Identifier of the message to get

    chat_id = None  # type: "int53"
    message_id = None  # type: "int53"


class getRepliedMessage(Method):
    # Returns information about a message that is replied by given
    # message, @chat_id Identifier of the chat the message belongs to
    # @message_id Identifier of the message reply to which get

    chat_id = None  # type: "int53"
    message_id = None  # type: "int53"


class getChatPinnedMessage(Method):
    # Returns information about a pinned chat message, @chat_id Identifier of
    # the chat the message belongs to

    chat_id = None  # type: "int53"


class getChatMessageByDate(Method):
    # Returns the last message sent in a chat no later
    # than the specified date, @chat_id Chat identifier, @date Point in
    # time (Unix timestamp) relative to which to search for messages

    chat_id = None  # type: "int53"
    date = None  # type: "int32"


class sendMessage(Method):
    # Sends a message. Returns the sent message, @chat_id Target chat
    # @reply_to_message_id Identifier of the message to reply to or 0

    chat_id = None  # type: "int53"
    reply_to_message_id = None  # type: "int53"
    disable_notification = None  # type: "Bool"
    from_background = None  # type: "Bool"
    reply_markup = None  # type: "ReplyMarkup"
    input_message_content = None  # type: "InputMessageContent"


class sendBotStartMessage(Method):
    # Invites a bot to a chat (if it is not
    # yet a member) and sends it the /start command. Bots
    # can't be invited to a private chat other than the
    # chat with the bot. Bots can't be invited to channels
    # (although they can be added as admins) and secret chats.
    # Returns the sent message

    bot_user_id = None  # type: "int32"
    chat_id = None  # type: "int53"
    parameter = None  # type: "string"


class sendInlineQueryResultMessage(Method):
    # Sends the result of an inline query as a message.
    # Returns the sent message. Always clears a chat draft message
    # @chat_id Target chat, @reply_to_message_id Identifier of a message to reply to or 0

    chat_id = None  # type: "int53"
    reply_to_message_id = None  # type: "int53"
    disable_notification = None  # type: "Bool"
    from_background = None  # type: "Bool"
    query_id = None  # type: "int64"
    result_id = None  # type: "string"


class sendChatSetTtlMessage(Method):
    # Changes the current TTL setting (sets a new self-destruct timer)
    # in a secret chat and sends the corresponding message, @chat_id
    # Chat identifier, @ttl New TTL value, in seconds

    chat_id = None  # type: "int53"
    ttl = None  # type: "int32"


class addLocalMessage(Method):
    # Adds a local message to a chat. The message is
    # persistent across application restarts only if the message database is
    # used. Returns the added message, @chat_id Target chat, @sender_user_id Identifier
    # of the user who will be shown as the sender
    # of the message; may be 0 for channel posts

    chat_id = None  # type: "int53"
    sender_user_id = None  # type: "int32"
    reply_to_message_id = None  # type: "int53"
    disable_notification = None  # type: "Bool"
    input_message_content = None  # type: "InputMessageContent"


class editMessageText(Method):
    # Edits the text of a message (or a text of
    # a game message). Returns the edited message after the edit
    # is completed on the server side

    chat_id = None  # type: "int53"
    message_id = None  # type: "int53"
    reply_markup = None  # type: "ReplyMarkup"
    input_message_content = None  # type: "InputMessageContent"


class editMessageLiveLocation(Method):
    # Edits the message content of a live location. Messages can
    # be edited for a limited period of time specified in
    # the live location. Returns the edited message after the edit
    # is completed on the server side

    chat_id = None  # type: "int53"
    message_id = None  # type: "int53"
    reply_markup = None  # type: "ReplyMarkup"
    location = None  # type: "location"


class editMessageMedia(Method):
    # Edits the content of a message with an animation, an
    # audio, a document, a photo or a video. The media
    # in the message can't be replaced if the message was
    # set to self-destruct. Media can't be replaced by self-destructing media.
    # Media in an album can be edited only to contain
    # a photo or a video. Returns the edited message after
    # the edit is completed on the server side

    chat_id = None  # type: "int53"
    message_id = None  # type: "int53"
    reply_markup = None  # type: "ReplyMarkup"
    input_message_content = None  # type: "InputMessageContent"


class editMessageCaption(Method):
    # Edits the message content caption. Returns the edited message after
    # the edit is completed on the server side

    chat_id = None  # type: "int53"
    message_id = None  # type: "int53"
    reply_markup = None  # type: "ReplyMarkup"
    caption = None  # type: "formattedText"


class editMessageReplyMarkup(Method):
    # Edits the message reply markup; for bots only. Returns the
    # edited message after the edit is completed on the server side

    chat_id = None  # type: "int53"
    message_id = None  # type: "int53"
    reply_markup = None  # type: "ReplyMarkup"


class setGameScore(Method):
    # Updates the game score of the specified user in the
    # game; for bots only, @chat_id The chat to which the
    # message with the game, @message_id Identifier of the message, @edit_message
    # True, if the message should be edited, @user_id User identifier
    # @score The new score

    chat_id = None  # type: "int53"
    message_id = None  # type: "int53"
    edit_message = None  # type: "Bool"
    user_id = None  # type: "int32"
    score = None  # type: "int32"
    force = None  # type: "Bool"
