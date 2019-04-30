from ..factory import Method


class readFilePart(Method):
	file_id = None  # type: "int32"
	offset = None  # type: "int32"
	count = None  # type: "int32"
