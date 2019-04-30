from ..factory import Type


class pushMessageContentChatDeleteMember(Type):
	member_name = None  # type: "string"
	is_current_user = None  # type: "Bool"
	is_left = None  # type: "Bool"
