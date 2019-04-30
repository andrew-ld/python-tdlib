from ..factory import Type


class sticker(Type):
	set_id = None  # type: "int64"
	width = None  # type: "int32"
	height = None  # type: "int32"
	emoji = None  # type: "string"
	is_mask = None  # type: "Bool"
	mask_position = None  # type: "maskPosition"
	thumbnail = None  # type: "photoSize"
	sticker = None  # type: "file"
