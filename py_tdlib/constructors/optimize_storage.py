from ..factory import Method


class optimizeStorage(Method):
	size = None  # type: "int53"
	ttl = None  # type: "int32"
	count = None  # type: "int32"
	immunity_delay = None  # type: "int32"
	file_types = None  # type: "vector<FileType>"
	chat_ids = None  # type: "vector<int53>"
	exclude_chat_ids = None  # type: "vector<int53>"
	chat_limit = None  # type: "int32"
