from ..factory import Type


class chatMemberStatusAdministrator(Type):
	can_be_edited = None  # type: "Bool"
	can_change_info = None  # type: "Bool"
	can_post_messages = None  # type: "Bool"
	can_edit_messages = None  # type: "Bool"
	can_delete_messages = None  # type: "Bool"
	can_invite_users = None  # type: "Bool"
	can_restrict_members = None  # type: "Bool"
	can_pin_messages = None  # type: "Bool"
	can_promote_members = None  # type: "Bool"
