from ..factory import Type


class paymentResult(Type):
	success = None  # type: "Bool"
	verification_url = None  # type: "string"
