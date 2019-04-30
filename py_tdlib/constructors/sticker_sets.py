from ..factory import Type


class stickerSets(Type):
	total_count = None  # type: "int32"
	sets = None  # type: "vector<stickerSetInfo>"
