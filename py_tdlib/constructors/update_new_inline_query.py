from ..factory import Type


class updateNewInlineQuery(Type):
	id = None  # type: "int64"
	sender_user_id = None  # type: "int32"
	user_location = None  # type: "location"
	query = None  # type: "string"
	offset = None  # type: "string"
