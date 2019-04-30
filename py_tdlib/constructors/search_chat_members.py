from ..factory import Method


class searchChatMembers(Method):
	chat_id = None  # type: "int53"
	query = None  # type: "string"
	limit = None  # type: "int32"
	filter = None  # type: "ChatMembersFilter"
