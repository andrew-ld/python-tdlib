from ..factory import Method


class viewMessages(Method):
	chat_id = None  # type: "int53"
	message_ids = None  # type: "vector<int53>"
	force_read = None  # type: "Bool"
