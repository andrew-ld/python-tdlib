from ..factory import Type


class chatEventMessageEdited(Type):
	old_message = None  # type: "message"
	new_message = None  # type: "message"
