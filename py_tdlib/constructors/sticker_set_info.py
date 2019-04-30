from ..factory import Type


class stickerSetInfo(Type):
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
