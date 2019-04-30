from ..factory import Type


class webPageInstantView(Type):
	page_blocks = None  # type: "vector<PageBlock>"
	version = None  # type: "int32"
	url = None  # type: "string"
	is_rtl = None  # type: "Bool"
	is_full = None  # type: "Bool"
