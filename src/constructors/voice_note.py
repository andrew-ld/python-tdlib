from tdwrapper.factory import Type


class voiceNote(Type):
    #  a voice note. The voice note must be encoded
    #  the Opus codec, and stored inside an OGG container.
    #  notes can have only a single audio channel @duration
    #  of the voice note, in seconds; as defined by the sender

    duration = None  # type: "int32"
    waveform = None  # type: "bytes"
    mime_type = None  # type: "string"
    voice = None  # type: "file"
