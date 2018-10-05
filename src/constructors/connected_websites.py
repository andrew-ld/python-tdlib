from tdwrapper.factory import Method, Type


class connectedWebsites(Type):
    #  a list of websites the current user is logged
    #  with Telegram @websites List of connected websites

    websites = None  # type: "vector<connectedWebsite>"


class getConnectedWebsites(Method):
    #  all website where the current user used Telegram to log in

    pass
