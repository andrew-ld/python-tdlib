from ..factory import Type


class updateUserChatAction(Type):
	chat_id = None  # type: "int53"
	user_id = None  # type: "int32"
	action = None  # type: "ChatAction"
