from ..factory import Type


class updateMessageEdited(Type):
	chat_id = None  # type: "int53"
	message_id = None  # type: "int53"
	edit_date = None  # type: "int32"
	reply_markup = None  # type: "ReplyMarkup"
