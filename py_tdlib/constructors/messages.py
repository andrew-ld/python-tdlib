from ..factory import Type


class messages(Type):
	total_count = None  # type: "int32"
	messages = None  # type: "vector<message>"
