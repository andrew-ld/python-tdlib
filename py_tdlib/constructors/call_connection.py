from ..factory import Type


class callConnection(Type):
	id = None  # type: "int64"
	ip = None  # type: "string"
	ipv6 = None  # type: "string"
	port = None  # type: "int32"
	peer_tag = None  # type: "bytes"
