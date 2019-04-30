from ..factory import Method


class writeGeneratedFilePart(Method):
	generation_id = None  # type: "int64"
	offset = None  # type: "int32"
	data = None  # type: "bytes"
