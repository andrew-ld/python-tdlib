from ..factory import Type


class chatEvent(Type):
	id = None  # type: "int64"
	date = None  # type: "int32"
	user_id = None  # type: "int32"
	action = None  # type: "ChatEventAction"
