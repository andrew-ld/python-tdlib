from ..factory import Type


class scopeNotificationSettings(Type):
	mute_for = None  # type: "int32"
	sound = None  # type: "string"
	show_preview = None  # type: "Bool"
	disable_pinned_message_notifications = None  # type: "Bool"
	disable_mention_notifications = None  # type: "Bool"
