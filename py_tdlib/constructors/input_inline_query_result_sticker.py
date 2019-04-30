from ..factory import Type


class inputInlineQueryResultSticker(Type):
	id = None  # type: "string"
	thumbnail_url = None  # type: "string"
	sticker_url = None  # type: "string"
	sticker_width = None  # type: "int32"
	sticker_height = None  # type: "int32"
	reply_markup = None  # type: "ReplyMarkup"
	input_message_content = None  # type: "InputMessageContent"
