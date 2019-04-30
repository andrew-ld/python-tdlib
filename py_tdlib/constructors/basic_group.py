from ..factory import Type


class basicGroup(Type):
	id = None  # type: "int32"
	member_count = None  # type: "int32"
	status = None  # type: "ChatMemberStatus"
	everyone_is_administrator = None  # type: "Bool"
	is_active = None  # type: "Bool"
	upgraded_to_supergroup_id = None  # type: "int32"
