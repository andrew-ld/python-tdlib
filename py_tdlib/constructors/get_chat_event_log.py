from ..factory import Method


class getChatEventLog(Method):
	chat_id = None  # type: "int53"
	query = None  # type: "string"
	from_event_id = None  # type: "int64"
	limit = None  # type: "int32"
	filters = None  # type: "chatEventLogFilters"
	user_ids = None  # type: "vector<int32>"
