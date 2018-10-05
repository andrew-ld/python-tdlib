from ..factory import Method, Type


class supergroup(Type):
    #  a supergroup or channel with zero or more members
    #  in the case of channels). From the point of
    #  of the system, a channel is a special kind
    #  a supergroup: only administrators can post and see the
    #  of members, and posts from all administrators use the
    #  and photo of the channel instead of individual names
    #  profile photos. Unlike supergroups, channels can have an unlimited number of subscribers

    id = None  # type: "int32"
    username = None  # type: "string"
    date = None  # type: "int32"
    status = None  # type: "ChatMemberStatus"
    member_count = None  # type: "int32"
    anyone_can_invite = None  # type: "Bool"
    sign_messages = None  # type: "Bool"
    is_channel = None  # type: "Bool"
    is_verified = None  # type: "Bool"
    restriction_reason = None  # type: "string"


class getSupergroup(Method):
    #  information about a supergroup or channel by its identifier.
    #  is an offline request if the current user is
    #  a bot @supergroup_id Supergroup or channel identifier

    supergroup_id = None  # type: "int32"
