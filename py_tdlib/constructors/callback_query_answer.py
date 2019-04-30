from ..factory import Type


class callbackQueryAnswer(Type):
	text = None  # type: "string"
	show_alert = None  # type: "Bool"
	url = None  # type: "string"
