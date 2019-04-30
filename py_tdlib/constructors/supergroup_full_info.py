from ..factory import Type


class supergroupFullInfo(Type):
	description = None  # type: "string"
	member_count = None  # type: "int32"
	administrator_count = None  # type: "int32"
	restricted_count = None  # type: "int32"
	banned_count = None  # type: "int32"
	can_get_members = None  # type: "Bool"
	can_set_username = None  # type: "Bool"
	can_set_sticker_set = None  # type: "Bool"
	can_view_statistics = None  # type: "Bool"
	is_all_history_available = None  # type: "Bool"
	sticker_set_id = None  # type: "int64"
	invite_link = None  # type: "string"
	upgraded_from_basic_group_id = None  # type: "int32"
	upgraded_from_max_message_id = None  # type: "int53"
