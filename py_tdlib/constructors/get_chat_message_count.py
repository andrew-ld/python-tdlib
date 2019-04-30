from ..factory import Method


class getChatMessageCount(Method):
	chat_id = None  # type: "int53"
	filter = None  # type: "SearchMessagesFilter"
	return_local = None  # type: "Bool"
