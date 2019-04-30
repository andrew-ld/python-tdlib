from ..factory import Type


class pageBlockEmbeddedPost(Type):
	url = None  # type: "string"
	author = None  # type: "string"
	author_photo = None  # type: "photo"
	date = None  # type: "int32"
	page_blocks = None  # type: "vector<PageBlock>"
	caption = None  # type: "pageBlockCaption"
