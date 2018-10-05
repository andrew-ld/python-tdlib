from ..factory import Method, Type


class stickerEmojis(Type):
    # Represents a list of all emoji corresponding to a sticker
    # in a sticker set. The list is only for informational
    # purposes, because a sticker is always sent with a fixed
    # emoji from the corresponding Sticker object @emojis List of emojis

    emojis = None  # type: "vector<string>"


class getStickerEmojis(Method):
    # Returns emoji corresponding to a sticker @sticker Sticker file identifier

    sticker = None  # type: "InputFile"
