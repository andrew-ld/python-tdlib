from ..factory import Method


class downloadFile(Method):
	file_id = None  # type: "int32"
	priority = None  # type: "int32"
	offset = None  # type: "int32"
	limit = None  # type: "int32"
	synchronous = None  # type: "Bool"
