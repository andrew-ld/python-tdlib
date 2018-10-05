from tdwrapper.factory import Type


class connectionStateWaitingForNetwork(Type):
    #  waiting for the network to become available. Use SetNetworkType
    #  change the available network type

    pass


class connectionStateConnectingToProxy(Type):
    #  establishing a connection with a proxy server

    pass


class connectionStateConnecting(Type):
    #  establishing a connection to the Telegram servers

    pass


class connectionStateUpdating(Type):
    #  data received while the client was offline

    pass


class connectionStateReady(Type):
    #  is a working connection to the Telegram servers

    pass
