from ..factory import Type


class chatActionTyping(Type):
    # The user is typing a message

    pass


class chatActionRecordingVideo(Type):
    # The user is recording a video

    pass


class chatActionUploadingVideo(Type):
    # The user is uploading a video @progress Upload progress, as a percentage

    progress = None  # type: "int32"


class chatActionRecordingVoiceNote(Type):
    # The user is recording a voice note

    pass


class chatActionUploadingVoiceNote(Type):
    # The user is uploading a voice note @progress Upload progress, as a percentage

    progress = None  # type: "int32"


class chatActionUploadingPhoto(Type):
    # The user is uploading a photo @progress Upload progress, as a percentage

    progress = None  # type: "int32"


class chatActionUploadingDocument(Type):
    # The user is uploading a document @progress Upload progress, as a percentage

    progress = None  # type: "int32"


class chatActionChoosingLocation(Type):
    # The user is picking a location or venue to send

    pass


class chatActionChoosingContact(Type):
    # The user is picking a contact to send

    pass


class chatActionStartPlayingGame(Type):
    # The user has started to play a game

    pass


class chatActionRecordingVideoNote(Type):
    # The user is recording a video note

    pass


class chatActionUploadingVideoNote(Type):
    # The user is uploading a video note @progress Upload progress, as a percentage

    progress = None  # type: "int32"


class chatActionCancel(Type):
    # The user has cancelled the previous action

    pass
