from ..factory import Method


class editMessageCaption(Method):
	chat_id = None  # type: "int53"
	message_id = None  # type: "int53"
	reply_markup = None  # type: "ReplyMarkup"
	caption = None  # type: "formattedText"
