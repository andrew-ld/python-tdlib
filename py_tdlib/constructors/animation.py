from ..factory import Type


class animation(Type):
	duration = None  # type: "int32"
	width = None  # type: "int32"
	height = None  # type: "int32"
	file_name = None  # type: "string"
	mime_type = None  # type: "string"
	thumbnail = None  # type: "photoSize"
	animation = None  # type: "file"
