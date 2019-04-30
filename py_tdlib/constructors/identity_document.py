from ..factory import Type


class identityDocument(Type):
	number = None  # type: "string"
	expiry_date = None  # type: "date"
	front_side = None  # type: "datedFile"
	reverse_side = None  # type: "datedFile"
	selfie = None  # type: "datedFile"
	translation = None  # type: "vector<datedFile>"
