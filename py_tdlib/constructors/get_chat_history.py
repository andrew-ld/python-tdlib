from ..factory import Method


class getChatHistory(Method):
	chat_id = None  # type: "int53"
	from_message_id = None  # type: "int53"
	offset = None  # type: "int32"
	limit = None  # type: "int32"
	only_local = None  # type: "Bool"
