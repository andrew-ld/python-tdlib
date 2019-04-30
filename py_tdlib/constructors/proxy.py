from ..factory import Type


class proxy(Type):
	id = None  # type: "int32"
	server = None  # type: "string"
	port = None  # type: "int32"
	last_used_date = None  # type: "int32"
	is_enabled = None  # type: "Bool"
	type = None  # type: "ProxyType"
