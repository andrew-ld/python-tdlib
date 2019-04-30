from ..factory import Type


class passportElementError(Type):
	type = None  # type: "PassportElementType"
	message = None  # type: "string"
	source = None  # type: "PassportElementErrorSource"
