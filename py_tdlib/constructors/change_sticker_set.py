from ..factory import Method


class changeStickerSet(Method):
	set_id = None  # type: "int64"
	is_installed = None  # type: "Bool"
	is_archived = None  # type: "Bool"
