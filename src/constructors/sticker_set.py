from ..factory import Method, Type


class stickerSet(Type):
    #  a sticker set @id Identifier of the sticker set
    #  Title of the sticker set @name Name of the
    #  set @is_installed True, if the sticker set has been
    #  by the current user

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
    #  information about a sticker set by its identifier @set_id
    #  of the sticker set

    set_id = None  # type: "int64"


class searchStickerSet(Method):
    #  for a sticker set by its name @name Name
    #  the sticker set

    name = None  # type: "string"


class createNewStickerSet(Method):
    #  a new sticker set; for bots only. Returns the
    #  created sticker set @user_id Sticker set owner @title Sticker
    #  title; 1-64 characters @name Sticker set name. Can contain
    #  English letters, digits and underscores. Must end with *"_by_<bot
    #  (*<bot_username>* is case insensitive); 1-64 characters

    user_id = None  # type: "int32"
    title = None  # type: "string"
    name = None  # type: "string"
    is_masks = None  # type: "Bool"
    stickers = None  # type: "vector<inputSticker>"


class addStickerToSet(Method):
    #  a new sticker to a set; for bots only.
    #  the sticker set @user_id Sticker set owner @name Sticker
    #  name @sticker Sticker to add to the set

    user_id = None  # type: "int32"
    name = None  # type: "string"
    sticker = None  # type: "inputSticker"
