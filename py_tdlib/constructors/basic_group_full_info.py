from ..factory import Method, Type


class basicGroupFullInfo(Type):
    # Contains full information about a basic group, @creator_user_id User identifier
    # of the creator of the group; 0 if unknown, @members
    # Group members, @invite_link Invite link for this group; available only
    # for the group creator and only after it has been
    # generated at least once

    creator_user_id = None  # type: "int32"
    members = None  # type: "vector<chatMember>"
    invite_link = None  # type: "string"


class getBasicGroupFullInfo(Method):
    # Returns full information about a basic group by its identifier
    # @basic_group_id Basic group identifier

    basic_group_id = None  # type: "int32"
