from tdwrapper.factory import Type


class inputSticker(Type):
    #  a sticker that should be added to a sticker
    #  @png_sticker PNG image with the sticker; must be up
    #  512 kB in size and fit in a 512x512
    #  @emojis Emoji corresponding to the sticker @mask_position For masks,
    #  where the mask should be placed; may be null

    png_sticker = None  # type: "InputFile"
    emojis = None  # type: "string"
    mask_position = None  # type: "maskPosition"
