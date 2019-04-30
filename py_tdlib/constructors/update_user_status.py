from ..factory import Type


class updateUserStatus(Type):
	user_id = None  # type: "int32"
	status = None  # type: "UserStatus"
