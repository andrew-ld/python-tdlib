from ..factory import Type


class supergroup(Type):
	id = None  # type: "int32"
	username = None  # type: "string"
	date = None  # type: "int32"
	status = None  # type: "ChatMemberStatus"
	member_count = None  # type: "int32"
	anyone_can_invite = None  # type: "Bool"
	sign_messages = None  # type: "Bool"
	is_channel = None  # type: "Bool"
	is_verified = None  # type: "Bool"
	restriction_reason = None  # type: "string"
