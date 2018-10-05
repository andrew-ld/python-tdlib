from ..factory import Type


class fileTypeNone(Type):
    # The data is not a file

    pass


class fileTypeAnimation(Type):
    # The file is an animation

    pass


class fileTypeAudio(Type):
    # The file is an audio file

    pass


class fileTypeDocument(Type):
    # The file is a document

    pass


class fileTypePhoto(Type):
    # The file is a photo

    pass


class fileTypeProfilePhoto(Type):
    # The file is a profile photo

    pass


class fileTypeSecret(Type):
    # The file was sent to a secret chat (the file
    # type is not known to the server)

    pass


class fileTypeSecretThumbnail(Type):
    # The file is a thumbnail of a file from a secret chat

    pass


class fileTypeSecure(Type):
    # The file is a file from Secure storage used for
    # storing Telegram Passport files

    pass


class fileTypeSticker(Type):
    # The file is a sticker

    pass


class fileTypeThumbnail(Type):
    # The file is a thumbnail of another file

    pass


class fileTypeUnknown(Type):
    # The file type is not yet known

    pass


class fileTypeVideo(Type):
    # The file is a video

    pass


class fileTypeVideoNote(Type):
    # The file is a video note

    pass


class fileTypeVoiceNote(Type):
    # The file is a voice note

    pass


class fileTypeWallpaper(Type):
    # The file is a wallpaper

    pass
