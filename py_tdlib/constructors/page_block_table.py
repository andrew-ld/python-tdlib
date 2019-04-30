from ..factory import Type


class pageBlockTable(Type):
	caption = None  # type: "RichText"
	cells = None  # type: "vector<vector<pageBlockTableCell>>"
	is_bordered = None  # type: "Bool"
	is_striped = None  # type: "Bool"
