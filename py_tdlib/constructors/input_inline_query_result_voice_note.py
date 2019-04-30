from ..factory import Type


class inputInlineQueryResultVoiceNote(Type):
	id = None  # type: "string"
	title = None  # type: "string"
	voice_note_url = None  # type: "string"
	voice_note_duration = None  # type: "int32"
	reply_markup = None  # type: "ReplyMarkup"
	input_message_content = None  # type: "InputMessageContent"
