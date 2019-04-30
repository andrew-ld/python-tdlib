from ..factory import Type


class inlineQueryResultArticle(Type):
	id = None  # type: "string"
	url = None  # type: "string"
	hide_url = None  # type: "Bool"
	title = None  # type: "string"
	description = None  # type: "string"
	thumbnail = None  # type: "photoSize"
