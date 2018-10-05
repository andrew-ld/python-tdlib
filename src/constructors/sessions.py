from ..factory import Method, Type


class sessions(Type):
    #  a list of sessions @sessions List of sessions

    sessions = None  # type: "vector<session>"


class getActiveSessions(Method):
    #  all active sessions of the current user

    pass
