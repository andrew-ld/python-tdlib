from ..factory import Type


class audio(Type):
	duration = None  # type: "int32"
	title = None  # type: "string"
	performer = None  # type: "string"
	file_name = None  # type: "string"
	mime_type = None  # type: "string"
	album_cover_thumbnail = None  # type: "photoSize"
	audio = None  # type: "file"
