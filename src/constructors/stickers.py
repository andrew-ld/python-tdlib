from ..factory import Method, Type


class stickers(Type):
    #  a list of stickers @stickers List of stickers

    stickers = None  # type: "vector<sticker>"


class getStickers(Method):
    #  stickers from the installed sticker sets that correspond to
    #  given emoji. If the emoji is not empty, favorite
    #  recently used stickers may also be returned @emoji String
    #  of emoji. If empty, returns all known installed stickers
    #  Maximum number of stickers to be returned

    emoji = None  # type: "string"
    limit = None  # type: "int32"


class searchStickers(Method):
    #  for stickers from public sticker sets that correspond to
    #  given emoji @emoji String representation of emoji; must be
    #  @limit Maximum number of stickers to be returned

    emoji = None  # type: "string"
    limit = None  # type: "int32"


class getRecentStickers(Method):
    #  a list of recently used stickers @is_attached Pass true
    #  return stickers and masks that were recently attached to
    #  or video files; pass false to return recently sent

    is_attached = None  # type: "Bool"


class addRecentSticker(Method):
    #  adds a new sticker to the list of recently
    #  stickers. The new sticker is added to the top
    #  the list. If the sticker was already in the
    #  it is removed from the list first. Only stickers
    #  to a sticker set can be added to this

    is_attached = None  # type: "Bool"
    sticker = None  # type: "InputFile"


class getFavoriteStickers(Method):
    #  favorite stickers

    pass
