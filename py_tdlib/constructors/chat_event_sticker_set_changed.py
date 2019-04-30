from ..factory import Type


class chatEventStickerSetChanged(Type):
	old_sticker_set_id = None  # type: "int64"
	new_sticker_set_id = None  # type: "int64"
