from ..factory import Type


class messageInvoice(Type):
	title = None  # type: "string"
	description = None  # type: "string"
	photo = None  # type: "photo"
	currency = None  # type: "string"
	total_amount = None  # type: "int53"
	start_parameter = None  # type: "string"
	is_test = None  # type: "Bool"
	need_shipping_address = None  # type: "Bool"
	receipt_message_id = None  # type: "int53"
