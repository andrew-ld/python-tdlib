from ..factory import Method


class getInlineQueryResults(Method):
	bot_user_id = None  # type: "int32"
	chat_id = None  # type: "int53"
	user_location = None  # type: "location"
	query = None  # type: "string"
	offset = None  # type: "string"
