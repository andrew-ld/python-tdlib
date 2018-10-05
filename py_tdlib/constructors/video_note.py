from ..factory import Type


class videoNote(Type):
    #  a video note. The video must be equal in
    #  and height, cropped to a circle, and stored in
    #  format @duration Duration of the video, in seconds; as
    #  by the sender @length Video width and height; as
    #  by the sender @thumbnail Video thumbnail; as defined by
    #  sender; may be null @video File containing the video

    duration = None  # type: "int32"
    length = None  # type: "int32"
    thumbnail = None  # type: "photoSize"
    video = None  # type: "file"
