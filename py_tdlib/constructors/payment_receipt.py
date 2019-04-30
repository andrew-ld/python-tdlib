from ..factory import Type


class paymentReceipt(Type):
	date = None  # type: "int32"
	payments_provider_user_id = None  # type: "int32"
	invoice = None  # type: "invoice"
	order_info = None  # type: "orderInfo"
	shipping_option = None  # type: "shippingOption"
	credentials_title = None  # type: "string"
