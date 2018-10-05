from ..factory import Type


class chatPhoto(Type):
    # Describes the photo of a chat @small A small (160x160)
    # chat photo @big A big (640x640) chat photo

    small = None  # type: "file"
    big = None  # type: "file"
