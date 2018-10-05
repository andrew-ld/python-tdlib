from ..factory import Method, Type


class users(Type):
    # Represents a list of users, @total_count Approximate total count of
    # users found, @user_ids A list of user identifiers

    total_count = None  # type: "int32"
    user_ids = None  # type: "vector<int32>"


class getChatAdministrators(Method):
    # Returns a list of users who are administrators of the
    # chat, @chat_id Chat identifier

    chat_id = None  # type: "int53"


class getBlockedUsers(Method):
    # Returns users that were blocked by the current user, @offset
    # Number of users to skip in the result; must be
    # non-negative, @limit Maximum number of users to return; up to 100

    offset = None  # type: "int32"
    limit = None  # type: "int32"


class getContacts(Method):
    # Returns all user contacts

    pass


class searchContacts(Method):
    # Searches for the specified query in the first names, last
    # names and usernames of the known user contacts, @query Query
    # to search for; can be empty to return all contacts
    # @limit Maximum number of users to be returned

    query = None  # type: "string"
    limit = None  # type: "int32"


class getRecentInlineBots(Method):
    # Returns up to 20 recently used inline bots in the
    # order of their last usage

    pass
