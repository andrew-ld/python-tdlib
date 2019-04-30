from ..factory import Type


class inputInlineQueryResultLocation(Type):
	id = None  # type: "string"
	location = None  # type: "location"
	live_period = None  # type: "int32"
	title = None  # type: "string"
	thumbnail_url = None  # type: "string"
	thumbnail_width = None  # type: "int32"
	thumbnail_height = None  # type: "int32"
	reply_markup = None  # type: "ReplyMarkup"
	input_message_content = None  # type: "InputMessageContent"
