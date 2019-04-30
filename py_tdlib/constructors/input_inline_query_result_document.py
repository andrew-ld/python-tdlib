from ..factory import Type


class inputInlineQueryResultDocument(Type):
	id = None  # type: "string"
	title = None  # type: "string"
	description = None  # type: "string"
	document_url = None  # type: "string"
	mime_type = None  # type: "string"
	thumbnail_url = None  # type: "string"
	thumbnail_width = None  # type: "int32"
	thumbnail_height = None  # type: "int32"
	reply_markup = None  # type: "ReplyMarkup"
	input_message_content = None  # type: "InputMessageContent"
