from ..factory import Type


class tdlibParameters(Type):
	use_test_dc = None  # type: "Bool"
	database_directory = None  # type: "string"
	files_directory = None  # type: "string"
	use_file_database = None  # type: "Bool"
	use_chat_info_database = None  # type: "Bool"
	use_message_database = None  # type: "Bool"
	use_secret_chats = None  # type: "Bool"
	api_id = None  # type: "int32"
	api_hash = None  # type: "string"
	system_language_code = None  # type: "string"
	device_model = None  # type: "string"
	system_version = None  # type: "string"
	application_version = None  # type: "string"
	enable_storage_optimizer = None  # type: "Bool"
	ignore_file_names = None  # type: "Bool"
