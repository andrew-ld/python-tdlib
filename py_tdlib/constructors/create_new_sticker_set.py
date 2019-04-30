from ..factory import Method


class createNewStickerSet(Method):
	user_id = None  # type: "int32"
	title = None  # type: "string"
	name = None  # type: "string"
	is_masks = None  # type: "Bool"
	stickers = None  # type: "vector<inputSticker>"
