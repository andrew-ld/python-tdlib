from ..factory import Type


class messagePaymentSuccessfulBot(Type):
	invoice_message_id = None  # type: "int53"
	currency = None  # type: "string"
	total_amount = None  # type: "int53"
	invoice_payload = None  # type: "bytes"
	shipping_option_id = None  # type: "string"
	order_info = None  # type: "orderInfo"
	telegram_payment_charge_id = None  # type: "string"
	provider_payment_charge_id = None  # type: "string"
