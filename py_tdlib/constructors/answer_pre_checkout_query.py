from ..factory import Method


class answerPreCheckoutQuery(Method):
	pre_checkout_query_id = None  # type: "int64"
	error_message = None  # type: "string"
