from ..factory import Method


class getCallbackQueryAnswer(Method):
	chat_id = None  # type: "int53"
	message_id = None  # type: "int53"
	payload = None  # type: "CallbackQueryPayload"
