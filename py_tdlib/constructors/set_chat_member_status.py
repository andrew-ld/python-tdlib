from ..factory import Method


class setChatMemberStatus(Method):
	chat_id = None  # type: "int53"
	user_id = None  # type: "int32"
	status = None  # type: "ChatMemberStatus"
