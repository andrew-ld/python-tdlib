from ..factory import Method


class searchMessages(Method):
	query = None  # type: "string"
	offset_date = None  # type: "int32"
	offset_chat_id = None  # type: "int53"
	offset_message_id = None  # type: "int53"
	limit = None  # type: "int32"
