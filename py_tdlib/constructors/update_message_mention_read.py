from ..factory import Type


class updateMessageMentionRead(Type):
	chat_id = None  # type: "int53"
	message_id = None  # type: "int53"
	unread_mention_count = None  # type: "int32"
