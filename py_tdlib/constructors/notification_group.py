from ..factory import Type


class notificationGroup(Type):
	id = None  # type: "int32"
	type = None  # type: "NotificationGroupType"
	chat_id = None  # type: "int53"
	total_count = None  # type: "int32"
	notifications = None  # type: "vector<notification>"
