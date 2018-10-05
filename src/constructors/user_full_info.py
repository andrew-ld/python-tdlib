from ..factory import Method, Type


class userFullInfo(Type):
    #  full information about a user (except the full list
    #  profile photos) @is_blocked True, if the user is blacklisted
    #  the current user @can_be_called True, if the user can
    #  called @has_private_calls True, if the user can't be called
    #  to their privacy settings

    is_blocked = None  # type: "Bool"
    can_be_called = None  # type: "Bool"
    has_private_calls = None  # type: "Bool"
    bio = None  # type: "string"
    share_text = None  # type: "string"
    group_in_common_count = None  # type: "int32"
    bot_info = None  # type: "botInfo"


class getUserFullInfo(Method):
    #  full information about a user by their identifier @user_id User identifier

    user_id = None  # type: "int32"
