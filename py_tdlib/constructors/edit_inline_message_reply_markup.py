from ..factory import Method


class editInlineMessageReplyMarkup(Method):
	inline_message_id = None  # type: "string"
	reply_markup = None  # type: "ReplyMarkup"
