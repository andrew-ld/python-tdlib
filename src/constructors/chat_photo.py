from tdwrapper.factory import Type


class chatPhoto(Type):
    #  the photo of a chat @small A small (160x160)
    #  photo @big A big (640x640) chat photo

    small = None  # type: "file"
    big = None  # type: "file"
