from ..factory import Method, Type


class proxies(Type):
    # Represents a list of proxy servers, @proxies List of proxy servers

    proxies = None  # type: "vector<proxy>"


class getProxies(Method):
    # Returns list of proxies that are currently set up. Can
    # be called before authorization

    pass
