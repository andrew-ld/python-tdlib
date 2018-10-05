from ..factory import Type


class callConnection(Type):
    # Describes the address of UDP reflectors @id Reflector identifier @ip
    # IPv4 reflector address @ipv6 IPv6 reflector address @port Reflector port
    # number @peer_tag Connection peer tag

    id = None  # type: "int64"
    ip = None  # type: "string"
    ipv6 = None  # type: "string"
    port = None  # type: "int32"
    peer_tag = None  # type: "bytes"
