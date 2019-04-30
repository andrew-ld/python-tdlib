from ..factory import Method


class setBotUpdatesStatus(Method):
	pending_update_count = None  # type: "int32"
	error_message = None  # type: "string"
