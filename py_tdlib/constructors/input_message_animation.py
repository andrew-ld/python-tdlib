from ..factory import Type


class inputMessageAnimation(Type):
	animation = None  # type: "InputFile"
	thumbnail = None  # type: "inputThumbnail"
	duration = None  # type: "int32"
	width = None  # type: "int32"
	height = None  # type: "int32"
	caption = None  # type: "formattedText"
