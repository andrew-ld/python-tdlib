from ..factory import Type


class userStatusEmpty(Type):
    # The user status was never changed

    pass


class userStatusOnline(Type):
    # The user is online, @expires Point in time (Unix timestamp)
    # when the user's online status will expire

    expires = None  # type: "int32"


class userStatusOffline(Type):
    # The user is offline, @was_online Point in time (Unix timestamp)
    # when the user was last online

    was_online = None  # type: "int32"


class userStatusRecently(Type):
    # The user was online recently

    pass


class userStatusLastWeek(Type):
    # The user is offline, but was online last week

    pass


class userStatusLastMonth(Type):
    # The user is offline, but was online last month

    pass
