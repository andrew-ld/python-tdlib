from ..factory import Type


class game(Type):
	id = None  # type: "int64"
	short_name = None  # type: "string"
	title = None  # type: "string"
	text = None  # type: "formattedText"
	description = None  # type: "string"
	photo = None  # type: "photo"
	animation = None  # type: "animation"
