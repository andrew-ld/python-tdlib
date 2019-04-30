from ..factory import Type


class call(Type):
	id = None  # type: "int32"
	user_id = None  # type: "int32"
	is_outgoing = None  # type: "Bool"
	state = None  # type: "CallState"
