from ..factory import Method


class reportSupergroupSpam(Method):
	supergroup_id = None  # type: "int32"
	user_id = None  # type: "int32"
	message_ids = None  # type: "vector<int53>"
