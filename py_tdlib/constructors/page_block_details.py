from ..factory import Type


class pageBlockDetails(Type):
	header = None  # type: "RichText"
	page_blocks = None  # type: "vector<PageBlock>"
	is_open = None  # type: "Bool"
