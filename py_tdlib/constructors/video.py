from ..factory import Type


class video(Type):
    # Describes a video file, @duration Duration of the video, in
    # seconds; as defined by the sender, @width Video width; as
    # defined by the sender, @height Video height; as defined by the sender

    duration = None  # type: "int32"
    width = None  # type: "int32"
    height = None  # type: "int32"
    file_name = None  # type: "string"
    mime_type = None  # type: "string"
    has_stickers = None  # type: "Bool"
    supports_streaming = None  # type: "Bool"
    thumbnail = None  # type: "photoSize"
    video = None  # type: "file"
