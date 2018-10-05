from ..factory import Method, Type


class stickerSet(Type):
    # Represents a sticker set, @id Identifier of the sticker set
    # @title Title of the sticker set, @name Name of the
    # sticker set, @is_installed True, if the sticker set has been
    # installed by the current user

    id = None  # type: "int64"
    title = None  # type: "string"
    name = None  # type: "string"
    is_installed = None  # type: "Bool"
    is_archived = None  # type: "Bool"
    is_official = None  # type: "Bool"
    is_masks = None  # type: "Bool"
    is_viewed = None  # type: "Bool"
    stickers = None  # type: "vector<sticker>"
    emojis = None  # type: "vector<stickerEmojis>"


class getStickerSet(Method):
    # Returns information about a sticker set by its identifier, @set_id
    # Identifier of the sticker set

    set_id = None  # type: "int64"


class searchStickerSet(Method):
    # Searches for a sticker set by its name, @name Name
    # of the sticker set

    name = None  # type: "string"


class createNewStickerSet(Method):
    # Creates a new sticker set; for bots only. Returns the
    # newly created sticker set, @user_id Sticker set owner, @title Sticker
    # set title; 1-64 characters, @name Sticker set name. Can contain
    # only English letters, digits and underscores. Must end with *"_by_<bot
    # username>"* (*<bot_username>* is case insensitive); 1-64 characters

    user_id = None  # type: "int32"
    title = None  # type: "string"
    name = None  # type: "string"
    is_masks = None  # type: "Bool"
    stickers = None  # type: "vector<inputSticker>"


class addStickerToSet(Method):
    # Adds a new sticker to a set; for bots only.
    # Returns the sticker set, @user_id Sticker set owner, @name Sticker
    # set name, @sticker Sticker to add to the set

    user_id = None  # type: "int32"
    name = None  # type: "string"
    sticker = None  # type: "inputSticker"
