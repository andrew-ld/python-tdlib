from ..factory import Type


class authenticationCodeInfo(Type):
	phone_number = None  # type: "string"
	type = None  # type: "AuthenticationCodeType"
	next_type = None  # type: "AuthenticationCodeType"
	timeout = None  # type: "int32"
