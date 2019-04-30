from ..factory import Type


class networkStatisticsEntryCall(Type):
	network_type = None  # type: "NetworkType"
	sent_bytes = None  # type: "int53"
	received_bytes = None  # type: "int53"
	duration = None  # type: "double"
