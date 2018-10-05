from ..factory import Method, Type


class chats(Type):
    #  a list of chats @chat_ids List of chat identifiers

    chat_ids = None  # type: "vector<int53>"


class getChats(Method):
    #  an ordered list of chats. Chats are sorted by
    #  pair (order, chat_id) in decreasing order. (For example, to
    #  a list of chats from the beginning, the offset_order
    #  be equal to 2^63 - 1).

    offset_order = None  # type: "int64"
    offset_chat_id = None  # type: "int53"
    limit = None  # type: "int32"


class searchPublicChats(Method):
    #  public chats by looking for specified query in their
    #  and title. Currently only private chats, supergroups and channels
    #  be public. Returns a meaningful number of results. Returns
    #  if the length of the searched username prefix is
    #  than 5. Excludes private chats with contacts and chats
    #  the chat list from the results @query Query to search for

    query = None  # type: "string"


class searchChats(Method):
    #  for the specified query in the title and username
    #  already known chats, this is an offline request. Returns
    #  in the order seen in the chat list @query
    #  to search for. If the query is empty, returns
    #  to 20 recently found chats @limit Maximum number of
    #  to be returned

    query = None  # type: "string"
    limit = None  # type: "int32"


class searchChatsOnServer(Method):
    #  for the specified query in the title and username
    #  already known chats via request to the server. Returns
    #  in the order seen in the chat list @query
    #  to search for @limit Maximum number of chats to be returned

    query = None  # type: "string"
    limit = None  # type: "int32"


class getTopChats(Method):
    #  a list of frequently used chats. Supported only if
    #  chat info database is enabled @category Category of chats
    #  be returned @limit Maximum number of chats to be
    #  up to 30

    category = None  # type: "TopChatCategory"
    limit = None  # type: "int32"


class getCreatedPublicChats(Method):
    #  a list of public chats created by the user

    pass


class getGroupsInCommon(Method):
    #  a list of common chats with a given user.
    #  are sorted by their type and creation date @user_id
    #  identifier @offset_chat_id Chat identifier starting from which to return
    #  use 0 for the first request @limit Maximum number
    #  chats to be returned; up to 100

    user_id = None  # type: "int32"
    offset_chat_id = None  # type: "int53"
    limit = None  # type: "int32"
