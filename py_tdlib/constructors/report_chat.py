from ..factory import Method


class reportChat(Method):
	chat_id = None  # type: "int53"
	reason = None  # type: "ChatReportReason"
	message_ids = None  # type: "vector<int53>"
