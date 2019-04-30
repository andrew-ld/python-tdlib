from ..factory import Method


class setPassword(Method):
	old_password = None  # type: "string"
	new_password = None  # type: "string"
	new_hint = None  # type: "string"
	set_recovery_email_address = None  # type: "Bool"
	new_recovery_email_address = None  # type: "string"
