from ..factory import Type


class updateNewPreCheckoutQuery(Type):
	id = None  # type: "int64"
	sender_user_id = None  # type: "int32"
	currency = None  # type: "string"
	total_amount = None  # type: "int53"
	invoice_payload = None  # type: "bytes"
	shipping_option_id = None  # type: "string"
	order_info = None  # type: "orderInfo"
