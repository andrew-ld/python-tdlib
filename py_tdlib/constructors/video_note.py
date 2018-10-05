from ..factory import Type


class videoNote(Type):
    # Describes a video note. The video must be equal in
    # width and height, cropped to a circle, and stored in
    # MPEG4 format, @duration Duration of the video, in seconds; as
    # defined by the sender, @length Video width and height; as
    # defined by the sender, @thumbnail Video thumbnail; as defined by
    # the sender; may be null, @video File containing the video

    duration = None  # type: "int32"
    length = None  # type: "int32"
    thumbnail = None  # type: "photoSize"
    video = None  # type: "file"
