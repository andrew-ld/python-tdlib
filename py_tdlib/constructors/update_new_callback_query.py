from ..factory import Type


class updateNewCallbackQuery(Type):
	id = None  # type: "int64"
	sender_user_id = None  # type: "int32"
	chat_id = None  # type: "int53"
	message_id = None  # type: "int53"
	chat_instance = None  # type: "int64"
	payload = None  # type: "CallbackQueryPayload"
