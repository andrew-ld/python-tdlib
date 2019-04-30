from ..factory import Method


class addStickerToSet(Method):
	user_id = None  # type: "int32"
	name = None  # type: "string"
	sticker = None  # type: "inputSticker"
