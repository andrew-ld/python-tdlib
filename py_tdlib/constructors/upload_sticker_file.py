from ..factory import Method


class uploadStickerFile(Method):
	user_id = None  # type: "int32"
	png_sticker = None  # type: "InputFile"
