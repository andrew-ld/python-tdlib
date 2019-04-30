from ..factory import Type


class chatMember(Type):
	user_id = None  # type: "int32"
	inviter_user_id = None  # type: "int32"
	joined_chat_date = None  # type: "int32"
	status = None  # type: "ChatMemberStatus"
	bot_info = None  # type: "botInfo"
