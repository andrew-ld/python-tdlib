from ..factory import Type


class voiceNote(Type):
	duration = None  # type: "int32"
	waveform = None  # type: "bytes"
	mime_type = None  # type: "string"
	voice = None  # type: "file"
