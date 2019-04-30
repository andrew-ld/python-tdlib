from ..factory import Type


class networkStatisticsEntryFile(Type):
	file_type = None  # type: "FileType"
	network_type = None  # type: "NetworkType"
	sent_bytes = None  # type: "int53"
	received_bytes = None  # type: "int53"
