from ..factory import Method


class editProxy(Method):
	proxy_id = None  # type: "int32"
	server = None  # type: "string"
	port = None  # type: "int32"
	enable = None  # type: "Bool"
	type = None  # type: "ProxyType"
