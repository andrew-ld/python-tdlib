from ..factory import Type


class userFullInfo(Type):
	is_blocked = None  # type: "Bool"
	can_be_called = None  # type: "Bool"
	has_private_calls = None  # type: "Bool"
	bio = None  # type: "string"
	share_text = None  # type: "string"
	group_in_common_count = None  # type: "int32"
	bot_info = None  # type: "botInfo"
