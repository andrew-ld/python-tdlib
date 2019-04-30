from ..factory import Method


class searchChatMessages(Method):
	chat_id = None  # type: "int53"
	query = None  # type: "string"
	sender_user_id = None  # type: "int32"
	from_message_id = None  # type: "int53"
	offset = None  # type: "int32"
	limit = None  # type: "int32"
	filter = None  # type: "SearchMessagesFilter"
