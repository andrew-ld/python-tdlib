from ..factory import Method


class searchCallMessages(Method):
	from_message_id = None  # type: "int53"
	limit = None  # type: "int32"
	only_missed = None  # type: "Bool"
