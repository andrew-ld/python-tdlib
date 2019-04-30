from ..factory import Method


class toggleSupergroupInvites(Method):
	supergroup_id = None  # type: "int32"
	anyone_can_invite = None  # type: "Bool"
