from ..factory import Method, Type


class chatEvents(Type):
    # Contains a list of chat events @events List of events

    events = None  # type: "vector<chatEvent>"


class getChatEventLog(Method):
    # Returns a list of service actions taken by chat members
    # and administrators in the last 48 hours. Available only in
    # supergroups and channels. Requires administrator rights. Returns results in reverse
    # chronological order (i. e., in order of decreasing event_id)

    chat_id = None  # type: "int53"
    query = None  # type: "string"
    from_event_id = None  # type: "int64"
    limit = None  # type: "int32"
    filters = None  # type: "chatEventLogFilters"
    user_ids = None  # type: "vector<int32>"
