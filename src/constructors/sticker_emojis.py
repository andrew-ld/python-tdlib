from tdwrapper.factory import Method, Type


class stickerEmojis(Type):
    #  a list of all emoji corresponding to a sticker
    #  a sticker set. The list is only for informational
    #  because a sticker is always sent with a fixed
    #  from the corresponding Sticker object @emojis List of emojis

    emojis = None  # type: "vector<string>"


class getStickerEmojis(Method):
    #  emoji corresponding to a sticker @sticker Sticker file identifier

    sticker = None  # type: "InputFile"
