from ..factory import Type


class pageBlockTableCell(Type):
	text = None  # type: "RichText"
	is_header = None  # type: "Bool"
	colspan = None  # type: "int32"
	rowspan = None  # type: "int32"
	align = None  # type: "PageBlockHorizontalAlignment"
	valign = None  # type: "PageBlockVerticalAlignment"
