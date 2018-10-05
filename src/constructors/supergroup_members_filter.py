from tdwrapper.factory import Type


class supergroupMembersFilterRecent(Type):
    #  recently active users in reverse chronological order

    pass


class supergroupMembersFilterAdministrators(Type):
    #  the creator and administrators

    pass


class supergroupMembersFilterSearch(Type):
    #  to search for supergroup or channel members via a
    #  query @query Query to search for

    query = None  # type: "string"


class supergroupMembersFilterRestricted(Type):
    #  restricted supergroup members; can be used only by administrators
    #  Query to search for

    query = None  # type: "string"


class supergroupMembersFilterBanned(Type):
    #  users banned from the supergroup or channel; can be
    #  only by administrators @query Query to search for

    query = None  # type: "string"


class supergroupMembersFilterBots(Type):
    #  bot members of the supergroup or channel

    pass
