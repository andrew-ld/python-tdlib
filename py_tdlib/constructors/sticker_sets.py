from ..factory import Method, Type


class stickerSets(Type):
    # Represents a list of sticker sets, @total_count Approximate total number
    # of sticker sets found, @sets List of sticker sets

    total_count = None  # type: "int32"
    sets = None  # type: "vector<stickerSetInfo>"


class getInstalledStickerSets(Method):
    # Returns a list of installed sticker sets, @is_masks Pass true
    # to return mask sticker sets; pass false to return ordinary sticker sets

    is_masks = None  # type: "Bool"


class getArchivedStickerSets(Method):
    # Returns a list of archived sticker sets, @is_masks Pass true
    # to return mask stickers sets; pass false to return ordinary
    # sticker sets, @offset_sticker_set_id Identifier of the sticker set from which
    # to return the result, @limit Maximum number of sticker sets to return

    is_masks = None  # type: "Bool"
    offset_sticker_set_id = None  # type: "int64"
    limit = None  # type: "int32"


class getTrendingStickerSets(Method):
    # Returns a list of trending sticker sets

    pass


class getAttachedStickerSets(Method):
    # Returns a list of sticker sets attached to a file.
    # Currently only photos and videos can have attached sticker sets, @file_id File identifier

    file_id = None  # type: "int32"


class searchInstalledStickerSets(Method):
    # Searches for installed sticker sets by looking for specified query
    # in their title and name, @is_masks Pass true to return
    # mask sticker sets; pass false to return ordinary sticker sets
    # @query Query to search for, @limit Maximum number of sticker sets to return

    is_masks = None  # type: "Bool"
    query = None  # type: "string"
    limit = None  # type: "int32"


class searchStickerSets(Method):
    # Searches for ordinary sticker sets by looking for specified query
    # in their title and name. Excludes installed sticker sets from
    # the results, @query Query to search for

    query = None  # type: "string"
