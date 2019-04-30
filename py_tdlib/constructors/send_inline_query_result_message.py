from ..factory import Method


class sendInlineQueryResultMessage(Method):
	chat_id = None  # type: "int53"
	reply_to_message_id = None  # type: "int53"
	disable_notification = None  # type: "Bool"
	from_background = None  # type: "Bool"
	query_id = None  # type: "int64"
	result_id = None  # type: "string"
	hide_via_bot = None  # type: "Bool"
