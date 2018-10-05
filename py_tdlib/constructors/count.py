from ..factory import Method, Type


class count(Type):
    # Contains a counter, @count Count

    count = None  # type: "int32"


class getChatMessageCount(Method):
    # Returns approximate number of messages of the specified type in
    # the chat, @chat_id Identifier of the chat in which to
    # count messages, @filter Filter for message content; searchMessagesFilterEmpty is unsupported
    # in this function, @return_local If true, returns count that is
    # available locally without sending network requests, returning -1 if the
    # number of messages is unknown

    chat_id = None  # type: "int53"
    filter = None  # type: "SearchMessagesFilter"
    return_local = None  # type: "Bool"


class getImportedContactCount(Method):
    # Returns the total number of imported contacts

    pass
