from ..factory import Type


class inputMessageInvoice(Type):
	invoice = None  # type: "invoice"
	title = None  # type: "string"
	description = None  # type: "string"
	photo_url = None  # type: "string"
	photo_size = None  # type: "int32"
	photo_width = None  # type: "int32"
	photo_height = None  # type: "int32"
	payload = None  # type: "bytes"
	provider_token = None  # type: "string"
	provider_data = None  # type: "string"
	start_parameter = None  # type: "string"
