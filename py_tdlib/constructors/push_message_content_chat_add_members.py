from ..factory import Type


class pushMessageContentChatAddMembers(Type):
	member_name = None  # type: "string"
	is_current_user = None  # type: "Bool"
	is_returned = None  # type: "Bool"
