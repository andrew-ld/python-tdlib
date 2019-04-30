from ..factory import Method


class validateOrderInfo(Method):
	chat_id = None  # type: "int53"
	message_id = None  # type: "int53"
	order_info = None  # type: "orderInfo"
	allow_save = None  # type: "Bool"
