from ..factory import Method


class answerShippingQuery(Method):
	shipping_query_id = None  # type: "int64"
	shipping_options = None  # type: "vector<shippingOption>"
	error_message = None  # type: "string"
