from ..factory import Type


class passwordState(Type):
	has_password = None  # type: "Bool"
	password_hint = None  # type: "string"
	has_recovery_email_address = None  # type: "Bool"
	has_passport_data = None  # type: "Bool"
	recovery_email_address_code_info = None  # type: "emailAddressAuthenticationCodeInfo"
