from tdwrapper.factory import Type


class proxyTypeSocks5(Type):
    #  SOCKS5 proxy server @username Username for logging in; may
    #  empty @password Password for logging in; may be empty

    username = None  # type: "string"
    password = None  # type: "string"


class proxyTypeHttp(Type):
    #  HTTP transparent proxy server @username Username for logging in;
    #  be empty @password Password for logging in; may be
    #  @http_only Pass true, if the proxy supports only HTTP
    #  and doesn't support transparent TCP connections via HTTP CONNECT

    username = None  # type: "string"
    password = None  # type: "string"
    http_only = None  # type: "Bool"


class proxyTypeMtproto(Type):
    #  MTProto proxy server @secret The proxy's secret in hexadecimal

    secret = None  # type: "string"
