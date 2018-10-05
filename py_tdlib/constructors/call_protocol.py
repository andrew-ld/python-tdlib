from ..factory import Type


class callProtocol(Type):
    # Specifies the supported call protocols, @udp_p2p True, if UDP peer-to-peer
    # connections are supported, @udp_reflector True, if connection through UDP reflectors
    # is supported, @min_layer Minimum supported API layer; use 65, @max_layer
    # Maximum supported API layer; use 65

    udp_p2p = None  # type: "Bool"
    udp_reflector = None  # type: "Bool"
    min_layer = None  # type: "int32"
    max_layer = None  # type: "int32"
