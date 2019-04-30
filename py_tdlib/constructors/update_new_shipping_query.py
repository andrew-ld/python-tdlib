from ..factory import Type


class updateNewShippingQuery(Type):
	id = None  # type: "int64"
	sender_user_id = None  # type: "int32"
	invoice_payload = None  # type: "string"
	shipping_address = None  # type: "address"
