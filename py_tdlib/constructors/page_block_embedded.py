from ..factory import Type


class pageBlockEmbedded(Type):
	url = None  # type: "string"
	html = None  # type: "string"
	poster_photo = None  # type: "photo"
	width = None  # type: "int32"
	height = None  # type: "int32"
	caption = None  # type: "pageBlockCaption"
	is_full_width = None  # type: "Bool"
	allow_scrolling = None  # type: "Bool"
