from ..factory import Method


class sendCallRating(Method):
	call_id = None  # type: "int32"
	rating = None  # type: "int32"
	comment = None  # type: "string"
