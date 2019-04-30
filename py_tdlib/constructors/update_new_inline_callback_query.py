from ..factory import Type


class updateNewInlineCallbackQuery(Type):
	id = None  # type: "int64"
	sender_user_id = None  # type: "int32"
	inline_message_id = None  # type: "string"
	chat_instance = None  # type: "int64"
	payload = None  # type: "CallbackQueryPayload"
