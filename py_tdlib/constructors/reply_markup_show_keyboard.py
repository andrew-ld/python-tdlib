from ..factory import Type


class replyMarkupShowKeyboard(Type):
	rows = None  # type: "vector<vector<keyboardButton>>"
	resize_keyboard = None  # type: "Bool"
	one_time = None  # type: "Bool"
	is_personal = None  # type: "Bool"
