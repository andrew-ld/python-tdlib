from tdwrapper.factory import Type


class animation(Type):
    #  an animation file. The animation must be encoded in
    #  or MPEG4 format @duration Duration of the animation, in
    #  as defined by the sender @width Width of the
    #  @height Height of the animation

    duration = None  # type: "int32"
    width = None  # type: "int32"
    height = None  # type: "int32"
    file_name = None  # type: "string"
    mime_type = None  # type: "string"
    thumbnail = None  # type: "photoSize"
    animation = None  # type: "file"
