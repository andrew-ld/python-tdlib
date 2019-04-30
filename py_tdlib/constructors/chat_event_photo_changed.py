from ..factory import Type


class chatEventPhotoChanged(Type):
	old_photo = None  # type: "chatPhoto"
	new_photo = None  # type: "chatPhoto"
