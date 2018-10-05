from ..factory import Method, Type


class proxy(Type):
    # Contains information about a proxy server @id Unique identifier of
    # the proxy @server Proxy server IP address @port Proxy server
    # port @last_used_date Point in time (Unix timestamp) when the proxy
    # was last used; 0 if never @is_enabled True, if the
    # proxy is enabled now @type Type of the proxy

    id = None  # type: "int32"
    server = None  # type: "string"
    port = None  # type: "int32"
    last_used_date = None  # type: "int32"
    is_enabled = None  # type: "Bool"
    type = None  # type: "ProxyType"


class addProxy(Method):
    # Adds a proxy server for network requests. Can be called
    # before authorization @server Proxy server IP address @port Proxy server
    # port @enable True, if the proxy should be enabled @type Proxy type

    server = None  # type: "string"
    port = None  # type: "int32"
    enable = None  # type: "Bool"
    type = None  # type: "ProxyType"


class editProxy(Method):
    # Edits an existing proxy server for network requests. Can be
    # called before authorization @proxy_id Proxy identifier @server Proxy server IP
    # address @port Proxy server port @enable True, if the proxy
    # should be enabled @type Proxy type

    proxy_id = None  # type: "int32"
    server = None  # type: "string"
    port = None  # type: "int32"
    enable = None  # type: "Bool"
    type = None  # type: "ProxyType"
