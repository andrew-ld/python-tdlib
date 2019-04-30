from ..factory import Type


class storageStatisticsByFileType(Type):
	file_type = None  # type: "FileType"
	size = None  # type: "int53"
	count = None  # type: "int32"
