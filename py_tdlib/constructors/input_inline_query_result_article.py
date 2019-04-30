from ..factory import Type


class inputInlineQueryResultArticle(Type):
	id = None  # type: "string"
	url = None  # type: "string"
	hide_url = None  # type: "Bool"
	title = None  # type: "string"
	description = None  # type: "string"
	thumbnail_url = None  # type: "string"
	thumbnail_width = None  # type: "int32"
	thumbnail_height = None  # type: "int32"
	reply_markup = None  # type: "ReplyMarkup"
	input_message_content = None  # type: "InputMessageContent"
