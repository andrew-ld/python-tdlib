from ..factory import Type


class updateNewChosenInlineResult(Type):
	sender_user_id = None  # type: "int32"
	user_location = None  # type: "location"
	query = None  # type: "string"
	result_id = None  # type: "string"
	inline_message_id = None  # type: "string"
