from tdwrapper.factory import Method, Type


class networkStatistics(Type):
    #  full list of available network statistic entries @since_date Point
    #  time (Unix timestamp) when the app began collecting statistics
    #  Network statistics entries

    since_date = None  # type: "int32"
    entries = None  # type: "vector<NetworkStatisticsEntry>"


class getNetworkStatistics(Method):
    #  network data usage statistics. Can be called before authorization
    #  If true, returns only data for the current library

    only_current = None  # type: "Bool"
