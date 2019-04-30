from ..factory import Type


class messagePaymentSuccessful(Type):
	invoice_message_id = None  # type: "int53"
	currency = None  # type: "string"
	total_amount = None  # type: "int53"
