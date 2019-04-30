from ..factory import Method


class deleteMessages(Method):
	chat_id = None  # type: "int53"
	message_ids = None  # type: "vector<int53>"
	revoke = None  # type: "Bool"
