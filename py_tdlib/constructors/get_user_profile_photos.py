from ..factory import Method


class getUserProfilePhotos(Method):
	user_id = None  # type: "int32"
	offset = None  # type: "int32"
	limit = None  # type: "int32"
