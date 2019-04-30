from ..factory import Type


class inputMessageSticker(Type):
	sticker = None  # type: "InputFile"
	thumbnail = None  # type: "inputThumbnail"
	width = None  # type: "int32"
	height = None  # type: "int32"
