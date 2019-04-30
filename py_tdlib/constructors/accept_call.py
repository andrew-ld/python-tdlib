from ..factory import Method


class acceptCall(Method):
	call_id = None  # type: "int32"
	protocol = None  # type: "callProtocol"
