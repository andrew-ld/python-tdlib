from ..factory import Method, Type


class networkStatistics(Type):
    # A full list of available network statistic entries @since_date Point
    # in time (Unix timestamp) when the app began collecting statistics
    # @entries Network statistics entries

    since_date = None  # type: "int32"
    entries = None  # type: "vector<NetworkStatisticsEntry>"


class getNetworkStatistics(Method):
    # Returns network data usage statistics. Can be called before authorization
    # @only_current If true, returns only data for the current library launch

    only_current = None  # type: "Bool"
