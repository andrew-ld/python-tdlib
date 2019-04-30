from ..factory import Method


class editMessageMedia(Method):
	chat_id = None  # type: "int53"
	message_id = None  # type: "int53"
	reply_markup = None  # type: "ReplyMarkup"
	input_message_content = None  # type: "InputMessageContent"
