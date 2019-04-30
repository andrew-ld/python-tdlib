from ..factory import Type


class inputInlineQueryResultContact(Type):
	id = None  # type: "string"
	contact = None  # type: "contact"
	thumbnail_url = None  # type: "string"
	thumbnail_width = None  # type: "int32"
	thumbnail_height = None  # type: "int32"
	reply_markup = None  # type: "ReplyMarkup"
	input_message_content = None  # type: "InputMessageContent"
