from tdwrapper.factory import Method, Type


class proxies(Type):
    #  a list of proxy servers @proxies List of proxy

    proxies = None  # type: "vector<proxy>"


class getProxies(Method):
    #  list of proxies that are currently set up. Can
    #  called before authorization

    pass
