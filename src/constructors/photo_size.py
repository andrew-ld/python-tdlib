from tdwrapper.factory import Type


class photoSize(Type):
    #  description @type Thumbnail type (see https://core.telegram.org/constructor/photoSize) @photo Information about
    #  photo file @width Photo width @height Photo height

    type = None  # type: "string"
    photo = None  # type: "file"
    width = None  # type: "int32"
    height = None  # type: "int32"
