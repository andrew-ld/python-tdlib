from ..factory import Type


class inputMessageVideoNote(Type):
	video_note = None  # type: "InputFile"
	thumbnail = None  # type: "inputThumbnail"
	duration = None  # type: "int32"
	length = None  # type: "int32"
