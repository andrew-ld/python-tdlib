from ..factory import Method


class answerCallbackQuery(Method):
	callback_query_id = None  # type: "int64"
	text = None  # type: "string"
	show_alert = None  # type: "Bool"
	url = None  # type: "string"
	cache_time = None  # type: "int32"
