from ..factory import Type


class pushMessageContentPhoto(Type):
	photo = None  # type: "photo"
	caption = None  # type: "string"
	is_secret = None  # type: "Bool"
	is_pinned = None  # type: "Bool"
