from ..factory import Type


class chatEventUsernameChanged(Type):
	old_username = None  # type: "string"
	new_username = None  # type: "string"
