from ..factory import Type


class connectionStateWaitingForNetwork(Type):
    # Currently waiting for the network to become available. Use SetNetworkType
    # to change the available network type

    pass


class connectionStateConnectingToProxy(Type):
    # Currently establishing a connection with a proxy server

    pass


class connectionStateConnecting(Type):
    # Currently establishing a connection to the Telegram servers

    pass


class connectionStateUpdating(Type):
    # Downloading data received while the client was offline

    pass


class connectionStateReady(Type):
    # There is a working connection to the Telegram servers

    pass
