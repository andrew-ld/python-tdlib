from ..factory import Method


class sendPhoneNumberConfirmationCode(Method):
	hash = None  # type: "string"
	phone_number = None  # type: "string"
	allow_flash_call = None  # type: "Bool"
	is_current_phone_number = None  # type: "Bool"
