from ..factory import Method


class setAuthenticationPhoneNumber(Method):
	phone_number = None  # type: "string"
	allow_flash_call = None  # type: "Bool"
	is_current_phone_number = None  # type: "Bool"
