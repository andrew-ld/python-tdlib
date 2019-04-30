from ..factory import Type


class authorizationStateWaitCode(Type):
	is_registered = None  # type: "Bool"
	terms_of_service = None  # type: "termsOfService"
	code_info = None  # type: "authenticationCodeInfo"
