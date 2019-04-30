from ..factory import Type


class callProtocol(Type):
	udp_p2p = None  # type: "Bool"
	udp_reflector = None  # type: "Bool"
	min_layer = None  # type: "int32"
	max_layer = None  # type: "int32"
