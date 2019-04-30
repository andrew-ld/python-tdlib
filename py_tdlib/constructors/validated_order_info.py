from ..factory import Type


class validatedOrderInfo(Type):
	order_info_id = None  # type: "string"
	shipping_options = None  # type: "vector<shippingOption>"
