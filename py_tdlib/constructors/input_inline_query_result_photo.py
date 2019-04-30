from ..factory import Type


class inputInlineQueryResultPhoto(Type):
	id = None  # type: "string"
	title = None  # type: "string"
	description = None  # type: "string"
	thumbnail_url = None  # type: "string"
	photo_url = None  # type: "string"
	photo_width = None  # type: "int32"
	photo_height = None  # type: "int32"
	reply_markup = None  # type: "ReplyMarkup"
	input_message_content = None  # type: "InputMessageContent"
