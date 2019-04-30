from ..factory import Method


class saveApplicationLogEvent(Method):
	type = None  # type: "string"
	chat_id = None  # type: "int53"
	data = None  # type: "JsonValue"
