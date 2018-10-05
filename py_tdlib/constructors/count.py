from ..factory import Method, Type


class count(Type):
    #  a counter @count Count

    count = None  # type: "int32"


class getChatMessageCount(Method):
    #  approximate number of messages of the specified type in
    #  chat @chat_id Identifier of the chat in which to
    #  messages @filter Filter for message content; searchMessagesFilterEmpty is unsupported
    #  this function @return_local If true, returns count that is
    #  locally without sending network requests, returning -1 if the
    #  of messages is unknown

    chat_id = None  # type: "int53"
    filter = None  # type: "SearchMessagesFilter"
    return_local = None  # type: "Bool"


class getImportedContactCount(Method):
    #  the total number of imported contacts

    pass
