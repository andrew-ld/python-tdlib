from ..factory import Method


class addProxy(Method):
	server = None  # type: "string"
	port = None  # type: "int32"
	enable = None  # type: "Bool"
	type = None  # type: "ProxyType"
