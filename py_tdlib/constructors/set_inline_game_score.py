from ..factory import Method


class setInlineGameScore(Method):
	inline_message_id = None  # type: "string"
	edit_message = None  # type: "Bool"
	user_id = None  # type: "int32"
	score = None  # type: "int32"
	force = None  # type: "Bool"
