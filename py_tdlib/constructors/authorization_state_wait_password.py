from ..factory import Type


class authorizationStateWaitPassword(Type):
	password_hint = None  # type: "string"
	has_recovery_email_address = None  # type: "Bool"
	recovery_email_address_pattern = None  # type: "string"
