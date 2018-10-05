from ..factory import Type


class voiceNote(Type):
    # Describes a voice note. The voice note must be encoded
    # with the Opus codec, and stored inside an OGG container.
    # Voice notes can have only a single audio channel @duration
    # Duration of the voice note, in seconds; as defined by the sender

    duration = None  # type: "int32"
    waveform = None  # type: "bytes"
    mime_type = None  # type: "string"
    voice = None  # type: "file"
