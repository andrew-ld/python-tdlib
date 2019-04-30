from ..factory import Type


class inputMessageDocument(Type):
	document = None  # type: "InputFile"
	thumbnail = None  # type: "inputThumbnail"
	caption = None  # type: "formattedText"
