from ..factory import Type


class shippingOption(Type):
	id = None  # type: "string"
	title = None  # type: "string"
	price_parts = None  # type: "vector<labeledPricePart>"
