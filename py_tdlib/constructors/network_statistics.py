from ..factory import Type


class networkStatistics(Type):
	since_date = None  # type: "int32"
	entries = None  # type: "vector<NetworkStatisticsEntry>"
