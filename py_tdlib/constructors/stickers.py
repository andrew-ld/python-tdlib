from ..factory import Method, Type


class stickers(Type):
    # Represents a list of stickers @stickers List of stickers

    stickers = None  # type: "vector<sticker>"


class getStickers(Method):
    # Returns stickers from the installed sticker sets that correspond to
    # a given emoji. If the emoji is not empty, favorite
    # and recently used stickers may also be returned @emoji String
    # representation of emoji. If empty, returns all known installed stickers
    # @limit Maximum number of stickers to be returned

    emoji = None  # type: "string"
    limit = None  # type: "int32"


class searchStickers(Method):
    # Searches for stickers from public sticker sets that correspond to
    # a given emoji @emoji String representation of emoji; must be
    # non-empty @limit Maximum number of stickers to be returned

    emoji = None  # type: "string"
    limit = None  # type: "int32"


class getRecentStickers(Method):
    # Returns a list of recently used stickers @is_attached Pass true
    # to return stickers and masks that were recently attached to
    # photos or video files; pass false to return recently sent stickers

    is_attached = None  # type: "Bool"


class addRecentSticker(Method):
    # Manually adds a new sticker to the list of recently
    # used stickers. The new sticker is added to the top
    # of the list. If the sticker was already in the
    # list, it is removed from the list first. Only stickers
    # belonging to a sticker set can be added to this list

    is_attached = None  # type: "Bool"
    sticker = None  # type: "InputFile"


class getFavoriteStickers(Method):
    # Returns favorite stickers

    pass
