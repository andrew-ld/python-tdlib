from tdwrapper.factory import Type


class userStatusEmpty(Type):
    #  user status was never changed

    pass


class userStatusOnline(Type):
    #  user is online @expires Point in time (Unix timestamp)
    #  the user's online status will expire

    expires = None  # type: "int32"


class userStatusOffline(Type):
    #  user is offline @was_online Point in time (Unix timestamp)
    #  the user was last online

    was_online = None  # type: "int32"


class userStatusRecently(Type):
    #  user was online recently

    pass


class userStatusLastWeek(Type):
    #  user is offline, but was online last week

    pass


class userStatusLastMonth(Type):
    #  user is offline, but was online last month

    pass
