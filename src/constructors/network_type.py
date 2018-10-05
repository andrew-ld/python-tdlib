from tdwrapper.factory import Type


class networkTypeNone(Type):
    #  network is not available

    pass


class networkTypeMobile(Type):
    #  mobile network

    pass


class networkTypeMobileRoaming(Type):
    #  mobile roaming network

    pass


class networkTypeWiFi(Type):
    #  Wi-Fi network

    pass


class networkTypeOther(Type):
    #  different network type (e.g., Ethernet network)

    pass
