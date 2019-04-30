from ..factory import Type


class session(Type):
	id = None  # type: "int64"
	is_current = None  # type: "Bool"
	is_password_pending = None  # type: "Bool"
	api_id = None  # type: "int32"
	application_name = None  # type: "string"
	application_version = None  # type: "string"
	is_official_application = None  # type: "Bool"
	device_model = None  # type: "string"
	platform = None  # type: "string"
	system_version = None  # type: "string"
	log_in_date = None  # type: "int32"
	last_active_date = None  # type: "int32"
	ip = None  # type: "string"
	country = None  # type: "string"
	region = None  # type: "string"
