from ..factory import Method


class sendMessage(Method):
	chat_id = None  # type: "int53"
	reply_to_message_id = None  # type: "int53"
	disable_notification = None  # type: "Bool"
	from_background = None  # type: "Bool"
	reply_markup = None  # type: "ReplyMarkup"
	input_message_content = None  # type: "InputMessageContent"
