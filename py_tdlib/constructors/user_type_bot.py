from ..factory import Type


class userTypeBot(Type):
	can_join_groups = None  # type: "Bool"
	can_read_all_group_messages = None  # type: "Bool"
	is_inline = None  # type: "Bool"
	inline_query_placeholder = None  # type: "string"
	need_location = None  # type: "Bool"
