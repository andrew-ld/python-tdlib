from ..factory import Method


class setPassportElementErrors(Method):
	user_id = None  # type: "int32"
	errors = None  # type: "vector<inputPassportElementError>"
