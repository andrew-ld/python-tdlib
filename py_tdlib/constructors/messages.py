from ..factory import Method, Type


class messages(Type):
    # Contains a list of messages, @total_count Approximate total count of
    # messages found, @messages List of messages; messages may be null

    total_count = None  # type: "int32"
    messages = None  # type: "vector<message>"


class getMessages(Method):
    # Returns information about messages. If a message is not found,
    # returns null on the corresponding position of the result, @chat_id
    # Identifier of the chat the messages belong to, @message_ids Identifiers
    # of the messages to get

    chat_id = None  # type: "int53"
    message_ids = None  # type: "vector<int53>"


class getChatHistory(Method):
    # Returns messages in a chat. The messages are returned in
    # a reverse chronological order (i.e., in order of decreasing message_id).

    chat_id = None  # type: "int53"
    from_message_id = None  # type: "int53"
    offset = None  # type: "int32"
    limit = None  # type: "int32"
    only_local = None  # type: "Bool"


class searchChatMessages(Method):
    # Searches for messages with given words in the chat. Returns
    # the results in reverse chronological order, i.e. in order of
    # decreasing message_id. Cannot be used in secret chats with a non-empty query

    chat_id = None  # type: "int53"
    query = None  # type: "string"
    sender_user_id = None  # type: "int32"
    from_message_id = None  # type: "int53"
    offset = None  # type: "int32"
    limit = None  # type: "int32"
    filter = None  # type: "SearchMessagesFilter"


class searchMessages(Method):
    # Searches for messages in all chats except secret chats. Returns
    # the results in reverse chronological order (i.e., in order of
    # decreasing (date, chat_id, message_id)).

    query = None  # type: "string"
    offset_date = None  # type: "int32"
    offset_chat_id = None  # type: "int53"
    offset_message_id = None  # type: "int53"
    limit = None  # type: "int32"


class searchCallMessages(Method):
    # Searches for call messages. Returns the results in reverse chronological
    # order (i. e., in order of decreasing message_id). For optimal
    # performance the number of returned messages is chosen by the library

    from_message_id = None  # type: "int53"
    limit = None  # type: "int32"
    only_missed = None  # type: "Bool"


class searchChatRecentLocationMessages(Method):
    # Returns information about the recent locations of chat members that
    # were sent to the chat. Returns up to 1 location
    # message per user, @chat_id Chat identifier, @limit Maximum number of
    # messages to be returned

    chat_id = None  # type: "int53"
    limit = None  # type: "int32"


class getActiveLiveLocationMessages(Method):
    # Returns all active live locations that should be updated by
    # the client. The list is persistent across application restarts only
    # if the message database is used

    pass


class sendMessageAlbum(Method):
    # Sends messages grouped together into an album. Currently only photo
    # and video messages can be grouped into an album. Returns
    # sent messages, @chat_id Target chat, @reply_to_message_id Identifier of a message
    # to reply to or 0

    chat_id = None  # type: "int53"
    reply_to_message_id = None  # type: "int53"
    disable_notification = None  # type: "Bool"
    from_background = None  # type: "Bool"
    input_message_contents = None  # type: "vector<InputMessageContent>"


class forwardMessages(Method):
    # Forwards previously sent messages. Returns the forwarded messages in the
    # same order as the message identifiers passed in message_ids. If
    # a message can't be forwarded, null will be returned instead of the message

    chat_id = None  # type: "int53"
    from_chat_id = None  # type: "int53"
    message_ids = None  # type: "vector<int53>"
    disable_notification = None  # type: "Bool"
    from_background = None  # type: "Bool"
    as_album = None  # type: "Bool"
