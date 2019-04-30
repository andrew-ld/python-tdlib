from ..factory import Method


class toggleSupergroupSignMessages(Method):
	supergroup_id = None  # type: "int32"
	sign_messages = None  # type: "Bool"
