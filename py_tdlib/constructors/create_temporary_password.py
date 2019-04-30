from ..factory import Method


class createTemporaryPassword(Method):
	password = None  # type: "string"
	valid_for = None  # type: "int32"
