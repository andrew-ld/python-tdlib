from ..factory import Type


class poll(Type):
	id = None  # type: "int64"
	question = None  # type: "string"
	options = None  # type: "vector<pollOption>"
	total_voter_count = None  # type: "int32"
	is_closed = None  # type: "Bool"
