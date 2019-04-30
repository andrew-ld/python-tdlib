from ..factory import Method


class getArchivedStickerSets(Method):
	is_masks = None  # type: "Bool"
	offset_sticker_set_id = None  # type: "int64"
	limit = None  # type: "int32"
