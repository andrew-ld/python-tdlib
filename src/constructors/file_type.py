from ..factory import Type


class fileTypeNone(Type):
    #  data is not a file

    pass


class fileTypeAnimation(Type):
    #  file is an animation

    pass


class fileTypeAudio(Type):
    #  file is an audio file

    pass


class fileTypeDocument(Type):
    #  file is a document

    pass


class fileTypePhoto(Type):
    #  file is a photo

    pass


class fileTypeProfilePhoto(Type):
    #  file is a profile photo

    pass


class fileTypeSecret(Type):
    #  file was sent to a secret chat (the file
    #  is not known to the server)

    pass


class fileTypeSecretThumbnail(Type):
    #  file is a thumbnail of a file from a secret chat

    pass


class fileTypeSecure(Type):
    #  file is a file from Secure storage used for
    #  Telegram Passport files

    pass


class fileTypeSticker(Type):
    #  file is a sticker

    pass


class fileTypeThumbnail(Type):
    #  file is a thumbnail of another file

    pass


class fileTypeUnknown(Type):
    #  file type is not yet known

    pass


class fileTypeVideo(Type):
    #  file is a video

    pass


class fileTypeVideoNote(Type):
    #  file is a video note

    pass


class fileTypeVoiceNote(Type):
    #  file is a voice note

    pass


class fileTypeWallpaper(Type):
    #  file is a wallpaper

    pass
