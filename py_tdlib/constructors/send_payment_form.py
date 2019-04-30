from ..factory import Method


class sendPaymentForm(Method):
	chat_id = None  # type: "int53"
	message_id = None  # type: "int53"
	order_info_id = None  # type: "string"
	shipping_option_id = None  # type: "string"
	credentials = None  # type: "InputCredentials"
