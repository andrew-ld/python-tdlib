from ..factory import Method


class searchSecretMessages(Method):
	chat_id = None  # type: "int53"
	query = None  # type: "string"
	from_search_id = None  # type: "int64"
	limit = None  # type: "int32"
	filter = None  # type: "SearchMessagesFilter"
