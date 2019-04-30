from ..factory import Type


class passportElementsWithErrors(Type):
	elements = None  # type: "vector<PassportElement>"
	errors = None  # type: "vector<passportElementError>"
