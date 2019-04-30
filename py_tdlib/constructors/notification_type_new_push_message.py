from ..factory import Type


class notificationTypeNewPushMessage(Type):
	message_id = None  # type: "int53"
	sender_user_id = None  # type: "int32"
	content = None  # type: "PushMessageContent"
