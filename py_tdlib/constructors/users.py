from ..factory import Type


class users(Type):
	total_count = None  # type: "int32"
	user_ids = None  # type: "vector<int32>"
