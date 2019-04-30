from ..factory import Method


class cancelDownloadFile(Method):
	file_id = None  # type: "int32"
	only_if_pending = None  # type: "Bool"
