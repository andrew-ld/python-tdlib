from ..factory import Type


class inputInlineQueryResultAudio(Type):
	id = None  # type: "string"
	title = None  # type: "string"
	performer = None  # type: "string"
	audio_url = None  # type: "string"
	audio_duration = None  # type: "int32"
	reply_markup = None  # type: "ReplyMarkup"
	input_message_content = None  # type: "InputMessageContent"
