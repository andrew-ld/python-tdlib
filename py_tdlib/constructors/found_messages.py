from ..factory import Method, Type


class foundMessages(Type):
    # Contains a list of messages found by a search, @messages
    # List of messages, @next_from_search_id Value to pass as from_search_id to get more results

    messages = None  # type: "vector<message>"
    next_from_search_id = None  # type: "int64"


class searchSecretMessages(Method):
    # Searches for messages in secret chats. Returns the results in
    # reverse chronological order. For optimal performance the number of returned
    # messages is chosen by the library

    chat_id = None  # type: "int53"
    query = None  # type: "string"
    from_search_id = None  # type: "int64"
    limit = None  # type: "int32"
    filter = None  # type: "SearchMessagesFilter"
