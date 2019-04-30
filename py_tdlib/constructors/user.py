from ..factory import Type


class user(Type):
	id = None  # type: "int32"
	first_name = None  # type: "string"
	last_name = None  # type: "string"
	username = None  # type: "string"
	phone_number = None  # type: "string"
	status = None  # type: "UserStatus"
	profile_photo = None  # type: "profilePhoto"
	outgoing_link = None  # type: "LinkState"
	incoming_link = None  # type: "LinkState"
	is_verified = None  # type: "Bool"
	is_support = None  # type: "Bool"
	restriction_reason = None  # type: "string"
	have_access = None  # type: "Bool"
	type = None  # type: "UserType"
	language_code = None  # type: "string"
