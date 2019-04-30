from ..factory import Type


class storageStatisticsByChat(Type):
	chat_id = None  # type: "int53"
	size = None  # type: "int53"
	count = None  # type: "int32"
	by_file_type = None  # type: "vector<storageStatisticsByFileType>"
