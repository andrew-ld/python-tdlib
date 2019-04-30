from ..factory import Type


class chatInviteLinkInfo(Type):
	chat_id = None  # type: "int53"
	type = None  # type: "ChatType"
	title = None  # type: "string"
	photo = None  # type: "chatPhoto"
	member_count = None  # type: "int32"
	member_user_ids = None  # type: "vector<int32>"
	is_public = None  # type: "Bool"
