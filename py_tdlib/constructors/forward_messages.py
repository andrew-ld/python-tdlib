from ..factory import Method


class forwardMessages(Method):
	chat_id = None  # type: "int53"
	from_chat_id = None  # type: "int53"
	message_ids = None  # type: "vector<int53>"
	disable_notification = None  # type: "Bool"
	from_background = None  # type: "Bool"
	as_album = None  # type: "Bool"
