from ..factory import Method


class setGameScore(Method):
	chat_id = None  # type: "int53"
	message_id = None  # type: "int53"
	edit_message = None  # type: "Bool"
	user_id = None  # type: "int32"
	score = None  # type: "int32"
	force = None  # type: "Bool"
