from ..factory import Method


class sendPassportAuthorizationForm(Method):
	autorization_form_id = None  # type: "int32"
	types = None  # type: "vector<PassportElementType>"
