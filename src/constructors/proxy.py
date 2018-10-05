from tdwrapper.factory import Method, Type


class proxy(Type):
    #  information about a proxy server @id Unique identifier of
    #  proxy @server Proxy server IP address @port Proxy server
    #  @last_used_date Point in time (Unix timestamp) when the proxy
    #  last used; 0 if never @is_enabled True, if the
    #  is enabled now @type Type of the proxy

    id = None  # type: "int32"
    server = None  # type: "string"
    port = None  # type: "int32"
    last_used_date = None  # type: "int32"
    is_enabled = None  # type: "Bool"
    type = None  # type: "ProxyType"


class addProxy(Method):
    #  a proxy server for network requests. Can be called
    #  authorization @server Proxy server IP address @port Proxy server
    #  @enable True, if the proxy should be enabled @type Proxy type

    server = None  # type: "string"
    port = None  # type: "int32"
    enable = None  # type: "Bool"
    type = None  # type: "ProxyType"


class editProxy(Method):
    #  an existing proxy server for network requests. Can be
    #  before authorization @proxy_id Proxy identifier @server Proxy server IP
    #  @port Proxy server port @enable True, if the proxy
    #  be enabled @type Proxy type

    proxy_id = None  # type: "int32"
    server = None  # type: "string"
    port = None  # type: "int32"
    enable = None  # type: "Bool"
    type = None  # type: "ProxyType"
