from ..factory import Type


class passportAuthorizationForm(Type):
	id = None  # type: "int32"
	required_elements = None  # type: "vector<passportRequiredElement>"
	privacy_policy_url = None  # type: "string"
