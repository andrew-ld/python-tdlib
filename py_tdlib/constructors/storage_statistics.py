from ..factory import Type


class storageStatistics(Type):
	size = None  # type: "int53"
	count = None  # type: "int32"
	by_chat = None  # type: "vector<storageStatisticsByChat>"
