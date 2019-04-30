from ..factory import Type


class updateMessageSendFailed(Type):
	message = None  # type: "message"
	old_message_id = None  # type: "int53"
	error_code = None  # type: "int32"
	error_message = None  # type: "string"
