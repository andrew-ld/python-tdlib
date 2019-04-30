from ..factory import Method


class getInlineGameHighScores(Method):
	inline_message_id = None  # type: "string"
	user_id = None  # type: "int32"
