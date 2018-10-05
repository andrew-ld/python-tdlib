from ..factory import Method, Type


class basicGroupFullInfo(Type):
    #  full information about a basic group @creator_user_id User identifier
    #  the creator of the group; 0 if unknown @members
    #  members @invite_link Invite link for this group; available only
    #  the group creator and only after it has been
    #  at least once

    creator_user_id = None  # type: "int32"
    members = None  # type: "vector<chatMember>"
    invite_link = None  # type: "string"


class getBasicGroupFullInfo(Method):
    #  full information about a basic group by its identifier
    #  Basic group identifier

    basic_group_id = None  # type: "int32"
