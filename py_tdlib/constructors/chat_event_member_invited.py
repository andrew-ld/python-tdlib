from ..factory import Type


class chatEventMemberInvited(Type):
	user_id = None  # type: "int32"
	status = None  # type: "ChatMemberStatus"
