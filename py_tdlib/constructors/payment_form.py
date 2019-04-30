from ..factory import Type


class paymentForm(Type):
	invoice = None  # type: "invoice"
	url = None  # type: "string"
	payments_provider = None  # type: "paymentsProviderStripe"
	saved_order_info = None  # type: "orderInfo"
	saved_credentials = None  # type: "savedCredentials"
	can_save_credentials = None  # type: "Bool"
	need_password = None  # type: "Bool"
