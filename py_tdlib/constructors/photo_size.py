from ..factory import Type


class photoSize(Type):
    # Photo description @type Thumbnail type (see https://core.telegram.org/constructor/photoSize) @photo Information about
    # the photo file @width Photo width @height Photo height

    type = None  # type: "string"
    photo = None  # type: "file"
    width = None  # type: "int32"
    height = None  # type: "int32"
