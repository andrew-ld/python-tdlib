from ..factory import Type


class chatEventLogFilters(Type):
	message_edits = None  # type: "Bool"
	message_deletions = None  # type: "Bool"
	message_pins = None  # type: "Bool"
	member_joins = None  # type: "Bool"
	member_leaves = None  # type: "Bool"
	member_invites = None  # type: "Bool"
	member_promotions = None  # type: "Bool"
	member_restrictions = None  # type: "Bool"
	info_changes = None  # type: "Bool"
	setting_changes = None  # type: "Bool"
