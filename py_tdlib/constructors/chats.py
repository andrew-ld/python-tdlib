from ..factory import Method, Type


class chats(Type):
    # Represents a list of chats, @chat_ids List of chat identifiers

    chat_ids = None  # type: "vector<int53>"


class getChats(Method):
    # Returns an ordered list of chats. Chats are sorted by
    # the pair (order, chat_id) in decreasing order. (For example, to
    # get a list of chats from the beginning, the offset_order
    # should be equal to 2^63 - 1).

    offset_order = None  # type: "int64"
    offset_chat_id = None  # type: "int53"
    limit = None  # type: "int32"


class searchPublicChats(Method):
    # Searches public chats by looking for specified query in their
    # username and title. Currently only private chats, supergroups and channels
    # can be public. Returns a meaningful number of results. Returns
    # nothing if the length of the searched username prefix is
    # less than 5. Excludes private chats with contacts and chats
    # from the chat list from the results, @query Query to search for

    query = None  # type: "string"


class searchChats(Method):
    # Searches for the specified query in the title and username
    # of already known chats, this is an offline request. Returns
    # chats in the order seen in the chat list, @query
    # Query to search for. If the query is empty, returns
    # up to 20 recently found chats, @limit Maximum number of
    # chats to be returned

    query = None  # type: "string"
    limit = None  # type: "int32"


class searchChatsOnServer(Method):
    # Searches for the specified query in the title and username
    # of already known chats via request to the server. Returns
    # chats in the order seen in the chat list, @query
    # Query to search for, @limit Maximum number of chats to be returned

    query = None  # type: "string"
    limit = None  # type: "int32"


class getTopChats(Method):
    # Returns a list of frequently used chats. Supported only if
    # the chat info database is enabled, @category Category of chats
    # to be returned, @limit Maximum number of chats to be
    # returned; up to 30

    category = None  # type: "TopChatCategory"
    limit = None  # type: "int32"


class getCreatedPublicChats(Method):
    # Returns a list of public chats created by the user

    pass


class getGroupsInCommon(Method):
    # Returns a list of common chats with a given user.
    # Chats are sorted by their type and creation date, @user_id
    # User identifier, @offset_chat_id Chat identifier starting from which to return
    # chats; use 0 for the first request, @limit Maximum number
    # of chats to be returned; up to 100

    user_id = None  # type: "int32"
    offset_chat_id = None  # type: "int53"
    limit = None  # type: "int32"
