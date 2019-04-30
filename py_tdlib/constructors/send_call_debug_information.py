from ..factory import Method


class sendCallDebugInformation(Method):
	call_id = None  # type: "int32"
	debug_information = None  # type: "string"
