from ..factory import Type


class inputSticker(Type):
    # Describes a sticker that should be added to a sticker
    # set @png_sticker PNG image with the sticker; must be up
    # to 512 kB in size and fit in a 512x512
    # square @emojis Emoji corresponding to the sticker @mask_position For masks,
    # position where the mask should be placed; may be null

    png_sticker = None  # type: "InputFile"
    emojis = None  # type: "string"
    mask_position = None  # type: "maskPosition"
