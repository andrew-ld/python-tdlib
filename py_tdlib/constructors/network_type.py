from ..factory import Type


class networkTypeNone(Type):
    # The network is not available

    pass


class networkTypeMobile(Type):
    # A mobile network

    pass


class networkTypeMobileRoaming(Type):
    # A mobile roaming network

    pass


class networkTypeWiFi(Type):
    # A Wi-Fi network

    pass


class networkTypeOther(Type):
    # A different network type (e.g., Ethernet network)

    pass
