from ..factory import Type


class inputThumbnail(Type):
    # A thumbnail to be sent along with a file; should
    # be in JPEG or WEBP format for stickers, and less
    # than 200 kB in size, @thumbnail Thumbnail file to send.
    # Sending thumbnails by file_id is currently not supported

    thumbnail = None  # type: "InputFile"
    width = None  # type: "int32"
    height = None  # type: "int32"
