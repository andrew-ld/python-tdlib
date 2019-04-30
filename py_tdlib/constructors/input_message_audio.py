from ..factory import Type


class inputMessageAudio(Type):
	audio = None  # type: "InputFile"
	album_cover_thumbnail = None  # type: "inputThumbnail"
	duration = None  # type: "int32"
	title = None  # type: "string"
	performer = None  # type: "string"
	caption = None  # type: "formattedText"
