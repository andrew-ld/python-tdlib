from ..factory import Type


class inputMessagePhoto(Type):
	photo = None  # type: "InputFile"
	thumbnail = None  # type: "inputThumbnail"
	added_sticker_file_ids = None  # type: "vector<int32>"
	width = None  # type: "int32"
	height = None  # type: "int32"
	caption = None  # type: "formattedText"
	ttl = None  # type: "int32"
