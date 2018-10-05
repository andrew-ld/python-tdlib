from ..factory import Method, Type


class chatEvents(Type):
    #  a list of chat events @events List of events

    events = None  # type: "vector<chatEvent>"


class getChatEventLog(Method):
    #  a list of service actions taken by chat members
    #  administrators in the last 48 hours. Available only in
    #  and channels. Requires administrator rights. Returns results in reverse
    #  order (i. e., in order of decreasing event_id)

    chat_id = None  # type: "int53"
    query = None  # type: "string"
    from_event_id = None  # type: "int64"
    limit = None  # type: "int32"
    filters = None  # type: "chatEventLogFilters"
    user_ids = None  # type: "vector<int32>"
