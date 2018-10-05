from ..factory import Method, Type


class sessions(Type):
    # Contains a list of sessions @sessions List of sessions

    sessions = None  # type: "vector<session>"


class getActiveSessions(Method):
    # Returns all active sessions of the current user

    pass
