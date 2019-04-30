from ..factory import Method


class addLocalMessage(Method):
	chat_id = None  # type: "int53"
	sender_user_id = None  # type: "int32"
	reply_to_message_id = None  # type: "int53"
	disable_notification = None  # type: "Bool"
	input_message_content = None  # type: "InputMessageContent"
