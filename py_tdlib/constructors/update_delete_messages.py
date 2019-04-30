from ..factory import Type


class updateDeleteMessages(Type):
	chat_id = None  # type: "int53"
	message_ids = None  # type: "vector<int53>"
	is_permanent = None  # type: "Bool"
	from_cache = None  # type: "Bool"
