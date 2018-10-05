from ..factory import Type


class proxyTypeSocks5(Type):
    # A SOCKS5 proxy server @username Username for logging in; may
    # be empty @password Password for logging in; may be empty

    username = None  # type: "string"
    password = None  # type: "string"


class proxyTypeHttp(Type):
    # A HTTP transparent proxy server @username Username for logging in;
    # may be empty @password Password for logging in; may be
    # empty @http_only Pass true, if the proxy supports only HTTP
    # requests and doesn't support transparent TCP connections via HTTP CONNECT method

    username = None  # type: "string"
    password = None  # type: "string"
    http_only = None  # type: "Bool"


class proxyTypeMtproto(Type):
    # An MTProto proxy server @secret The proxy's secret in hexadecimal encoding

    secret = None  # type: "string"
