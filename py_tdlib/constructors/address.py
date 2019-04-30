from ..factory import Type


class address(Type):
	country_code = None  # type: "string"
	state = None  # type: "string"
	city = None  # type: "string"
	street_line1 = None  # type: "string"
	street_line2 = None  # type: "string"
	postal_code = None  # type: "string"
