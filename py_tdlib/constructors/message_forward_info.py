from ..factory import Type


class messageForwardInfo(Type):
	origin = None  # type: "MessageForwardOrigin"
	date = None  # type: "int32"
	from_chat_id = None  # type: "int53"
	from_message_id = None  # type: "int53"
