from ..factory import Method


class editInlineMessageLiveLocation(Method):
	inline_message_id = None  # type: "string"
	reply_markup = None  # type: "ReplyMarkup"
	location = None  # type: "location"
