from ..factory import Type


class inputMessageVideo(Type):
	video = None  # type: "InputFile"
	thumbnail = None  # type: "inputThumbnail"
	added_sticker_file_ids = None  # type: "vector<int32>"
	duration = None  # type: "int32"
	width = None  # type: "int32"
	height = None  # type: "int32"
	supports_streaming = None  # type: "Bool"
	caption = None  # type: "formattedText"
	ttl = None  # type: "int32"
