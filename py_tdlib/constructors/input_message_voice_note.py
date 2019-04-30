from ..factory import Type


class inputMessageVoiceNote(Type):
	voice_note = None  # type: "InputFile"
	duration = None  # type: "int32"
	waveform = None  # type: "bytes"
	caption = None  # type: "formattedText"
