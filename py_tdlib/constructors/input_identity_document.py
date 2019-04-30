from ..factory import Type


class inputIdentityDocument(Type):
	number = None  # type: "string"
	expiry_date = None  # type: "date"
	front_side = None  # type: "InputFile"
	reverse_side = None  # type: "InputFile"
	selfie = None  # type: "InputFile"
	translation = None  # type: "vector<InputFile>"
