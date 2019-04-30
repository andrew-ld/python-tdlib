from ..factory import Type


class encryptedPassportElement(Type):
	type = None  # type: "PassportElementType"
	data = None  # type: "bytes"
	front_side = None  # type: "datedFile"
	reverse_side = None  # type: "datedFile"
	selfie = None  # type: "datedFile"
	translation = None  # type: "vector<datedFile>"
	files = None  # type: "vector<datedFile>"
	value = None  # type: "string"
	hash = None  # type: "string"
