from tdwrapper.factory import Method, Type


class users(Type):
    #  a list of users @total_count Approximate total count of
    #  found @user_ids A list of user identifiers

    total_count = None  # type: "int32"
    user_ids = None  # type: "vector<int32>"


class getChatAdministrators(Method):
    #  a list of users who are administrators of the
    #  @chat_id Chat identifier

    chat_id = None  # type: "int53"


class getBlockedUsers(Method):
    #  users that were blocked by the current user @offset
    #  of users to skip in the result; must be
    #  @limit Maximum number of users to return; up to

    offset = None  # type: "int32"
    limit = None  # type: "int32"


class getContacts(Method):
    #  all user contacts

    pass


class searchContacts(Method):
    #  for the specified query in the first names, last
    #  and usernames of the known user contacts @query Query
    #  search for; can be empty to return all contacts
    #  Maximum number of users to be returned

    query = None  # type: "string"
    limit = None  # type: "int32"


class getRecentInlineBots(Method):
    #  up to 20 recently used inline bots in the
    #  of their last usage

    pass
