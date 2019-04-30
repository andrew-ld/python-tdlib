from ..factory import Type


class paymentsProviderStripe(Type):
	publishable_key = None  # type: "string"
	need_country = None  # type: "Bool"
	need_postal_code = None  # type: "Bool"
	need_cardholder_name = None  # type: "Bool"
