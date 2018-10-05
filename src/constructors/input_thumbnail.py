from ..factory import Type


class inputThumbnail(Type):
    #  thumbnail to be sent along with a file; should
    #  in JPEG or WEBP format for stickers, and less
    #  200 kB in size @thumbnail Thumbnail file to send.
    #  thumbnails by file_id is currently not supported

    thumbnail = None  # type: "InputFile"
    width = None  # type: "int32"
    height = None  # type: "int32"
