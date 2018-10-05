from ..factory import Method, Type


class basicGroup(Type):
    # Represents a basic group of 0-200 users (must be upgraded
    # to a supergroup to accommodate more than 200 users)

    id = None  # type: "int32"
    member_count = None  # type: "int32"
    status = None  # type: "ChatMemberStatus"
    everyone_is_administrator = None  # type: "Bool"
    is_active = None  # type: "Bool"
    upgraded_to_supergroup_id = None  # type: "int32"


class getBasicGroup(Method):
    # Returns information about a basic group by its identifier. This
    # is an offline request if the current user is not
    # a bot @basic_group_id Basic group identifier

    basic_group_id = None  # type: "int32"
