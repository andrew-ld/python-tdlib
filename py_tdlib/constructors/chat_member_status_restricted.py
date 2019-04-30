from ..factory import Type


class chatMemberStatusRestricted(Type):
	is_member = None  # type: "Bool"
	restricted_until_date = None  # type: "int32"
	can_send_messages = None  # type: "Bool"
	can_send_media_messages = None  # type: "Bool"
	can_send_other_messages = None  # type: "Bool"
	can_add_web_page_previews = None  # type: "Bool"
