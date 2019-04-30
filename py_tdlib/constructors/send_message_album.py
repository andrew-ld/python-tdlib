from ..factory import Method


class sendMessageAlbum(Method):
	chat_id = None  # type: "int53"
	reply_to_message_id = None  # type: "int53"
	disable_notification = None  # type: "Bool"
	from_background = None  # type: "Bool"
	input_message_contents = None  # type: "vector<InputMessageContent>"
