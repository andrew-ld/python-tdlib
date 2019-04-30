from ..factory import Type


class temporaryPasswordState(Type):
	has_password = None  # type: "Bool"
	valid_for = None  # type: "int32"
