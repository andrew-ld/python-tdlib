from ..factory import Type


class secretChat(Type):
	id = None  # type: "int32"
	user_id = None  # type: "int32"
	state = None  # type: "SecretChatState"
	is_outbound = None  # type: "Bool"
	ttl = None  # type: "int32"
	key_hash = None  # type: "bytes"
	layer = None  # type: "int32"
