from ..factory import Type


class basicGroupFullInfo(Type):
	creator_user_id = None  # type: "int32"
	members = None  # type: "vector<chatMember>"
	invite_link = None  # type: "string"
