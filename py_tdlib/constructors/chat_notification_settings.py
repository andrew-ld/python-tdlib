from ..factory import Type


class chatNotificationSettings(Type):
	use_default_mute_for = None  # type: "Bool"
	mute_for = None  # type: "int32"
	use_default_sound = None  # type: "Bool"
	sound = None  # type: "string"
	use_default_show_preview = None  # type: "Bool"
	show_preview = None  # type: "Bool"
	use_default_disable_pinned_message_notifications = None  # type: "Bool"
	disable_pinned_message_notifications = None  # type: "Bool"
	use_default_disable_mention_notifications = None  # type: "Bool"
	disable_mention_notifications = None  # type: "Bool"
