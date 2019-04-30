from ..factory import Type


class inputInlineQueryResultVideo(Type):
	id = None  # type: "string"
	title = None  # type: "string"
	description = None  # type: "string"
	thumbnail_url = None  # type: "string"
	video_url = None  # type: "string"
	mime_type = None  # type: "string"
	video_width = None  # type: "int32"
	video_height = None  # type: "int32"
	video_duration = None  # type: "int32"
	reply_markup = None  # type: "ReplyMarkup"
	input_message_content = None  # type: "InputMessageContent"
