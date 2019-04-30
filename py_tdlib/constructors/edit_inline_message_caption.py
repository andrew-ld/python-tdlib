from ..factory import Method


class editInlineMessageCaption(Method):
	inline_message_id = None  # type: "string"
	reply_markup = None  # type: "ReplyMarkup"
	caption = None  # type: "formattedText"
