from ..factory import Method


class uploadFile(Method):
	file = None  # type: "InputFile"
	file_type = None  # type: "FileType"
	priority = None  # type: "int32"
