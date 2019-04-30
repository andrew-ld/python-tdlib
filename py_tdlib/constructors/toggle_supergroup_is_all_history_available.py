from ..factory import Method


class toggleSupergroupIsAllHistoryAvailable(Method):
	supergroup_id = None  # type: "int32"
	is_all_history_available = None  # type: "Bool"
