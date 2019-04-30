from ..factory import Method


class editMessageLiveLocation(Method):
	chat_id = None  # type: "int53"
	message_id = None  # type: "int53"
	reply_markup = None  # type: "ReplyMarkup"
	location = None  # type: "location"
