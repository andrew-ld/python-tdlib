from tdwrapper.factory import Method, Type


class seconds(Type):
    #  a value representing a number of seconds @seconds Number of seconds

    seconds = None  # type: "double"


class pingProxy(Method):
    #  time needed to receive a response from a Telegram
    #  through a proxy. Can be called before authorization @proxy_id
    #  identifier. Use 0 to ping a Telegram server without a proxy

    proxy_id = None  # type: "int32"
