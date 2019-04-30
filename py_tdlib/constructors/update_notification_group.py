from ..factory import Type


class updateNotificationGroup(Type):
	notification_group_id = None  # type: "int32"
	type = None  # type: "NotificationGroupType"
	chat_id = None  # type: "int53"
	notification_settings_chat_id = None  # type: "int53"
	is_silent = None  # type: "Bool"
	total_count = None  # type: "int32"
	added_notifications = None  # type: "vector<notification>"
	removed_notification_ids = None  # type: "vector<int32>"
