from ..factory import Type


class updateChatReadInbox(Type):
	chat_id = None  # type: "int53"
	last_read_inbox_message_id = None  # type: "int53"
	unread_count = None  # type: "int32"
