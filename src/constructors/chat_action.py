from tdwrapper.factory import Type


class chatActionTyping(Type):
    #  user is typing a message

    pass


class chatActionRecordingVideo(Type):
    #  user is recording a video

    pass


class chatActionUploadingVideo(Type):
    #  user is uploading a video @progress Upload progress, as a percentage

    progress = None  # type: "int32"


class chatActionRecordingVoiceNote(Type):
    #  user is recording a voice note

    pass


class chatActionUploadingVoiceNote(Type):
    #  user is uploading a voice note @progress Upload progress, as a percentage

    progress = None  # type: "int32"


class chatActionUploadingPhoto(Type):
    #  user is uploading a photo @progress Upload progress, as a percentage

    progress = None  # type: "int32"


class chatActionUploadingDocument(Type):
    #  user is uploading a document @progress Upload progress, as a percentage

    progress = None  # type: "int32"


class chatActionChoosingLocation(Type):
    #  user is picking a location or venue to send

    pass


class chatActionChoosingContact(Type):
    #  user is picking a contact to send

    pass


class chatActionStartPlayingGame(Type):
    #  user has started to play a game

    pass


class chatActionRecordingVideoNote(Type):
    #  user is recording a video note

    pass


class chatActionUploadingVideoNote(Type):
    #  user is uploading a video note @progress Upload progress, as a percentage

    progress = None  # type: "int32"


class chatActionCancel(Type):
    #  user has cancelled the previous action

    pass
