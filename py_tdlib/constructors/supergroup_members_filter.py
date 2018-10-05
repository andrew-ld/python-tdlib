from ..factory import Type


class supergroupMembersFilterRecent(Type):
    # Returns recently active users in reverse chronological order

    pass


class supergroupMembersFilterAdministrators(Type):
    # Returns the creator and administrators

    pass


class supergroupMembersFilterSearch(Type):
    # Used to search for supergroup or channel members via a
    # (string) query, @query Query to search for

    query = None  # type: "string"


class supergroupMembersFilterRestricted(Type):
    # Returns restricted supergroup members; can be used only by administrators
    # @query Query to search for

    query = None  # type: "string"


class supergroupMembersFilterBanned(Type):
    # Returns users banned from the supergroup or channel; can be
    # used only by administrators, @query Query to search for

    query = None  # type: "string"


class supergroupMembersFilterBots(Type):
    # Returns bot members of the supergroup or channel

    pass
