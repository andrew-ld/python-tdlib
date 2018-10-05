from ..factory import Type


class stickerSetInfo(Type):
    # Represents short information about a sticker set @id Identifier of
    # the sticker set @title Title of the sticker set @name
    # Name of the sticker set @is_installed True, if the sticker
    # set has been installed by current user

    id = None  # type: "int64"
    title = None  # type: "string"
    name = None  # type: "string"
    is_installed = None  # type: "Bool"
    is_archived = None  # type: "Bool"
    is_official = None  # type: "Bool"
    is_masks = None  # type: "Bool"
    is_viewed = None  # type: "Bool"
    size = None  # type: "int32"
    covers = None  # type: "vector<sticker>"
