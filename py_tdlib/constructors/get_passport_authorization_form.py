from ..factory import Method


class getPassportAuthorizationForm(Method):
	bot_user_id = None  # type: "int32"
	scope = None  # type: "string"
	public_key = None  # type: "string"
	nonce = None  # type: "string"
