from ..factory import Method, Type


class connectedWebsites(Type):
    # Contains a list of websites the current user is logged
    # in with Telegram @websites List of connected websites

    websites = None  # type: "vector<connectedWebsite>"


class getConnectedWebsites(Method):
    # Returns all website where the current user used Telegram to log in

    pass
