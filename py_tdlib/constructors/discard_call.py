from ..factory import Method


class discardCall(Method):
	call_id = None  # type: "int32"
	is_disconnected = None  # type: "Bool"
	duration = None  # type: "int32"
	connection_id = None  # type: "int64"
