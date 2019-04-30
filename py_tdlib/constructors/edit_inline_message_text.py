from ..factory import Method


class editInlineMessageText(Method):
	inline_message_id = None  # type: "string"
	reply_markup = None  # type: "ReplyMarkup"
	input_message_content = None  # type: "InputMessageContent"
