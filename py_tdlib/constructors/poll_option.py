from ..factory import Type


class pollOption(Type):
	text = None  # type: "string"
	voter_count = None  # type: "int32"
	vote_percentage = None  # type: "int32"
	is_chosen = None  # type: "Bool"
	is_being_chosen = None  # type: "Bool"
