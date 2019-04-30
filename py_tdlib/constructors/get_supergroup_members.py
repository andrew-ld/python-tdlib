from ..factory import Method


class getSupergroupMembers(Method):
	supergroup_id = None  # type: "int32"
	filter = None  # type: "SupergroupMembersFilter"
	offset = None  # type: "int32"
	limit = None  # type: "int32"
