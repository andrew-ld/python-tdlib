from ..factory import Type


class pushMessageContentVideo(Type):
	video = None  # type: "video"
	caption = None  # type: "string"
	is_secret = None  # type: "Bool"
	is_pinned = None  # type: "Bool"
