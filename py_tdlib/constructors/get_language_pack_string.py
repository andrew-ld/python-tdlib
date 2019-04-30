from ..factory import Method


class getLanguagePackString(Method):
	language_pack_database_path = None  # type: "string"
	localization_target = None  # type: "string"
	language_pack_id = None  # type: "string"
	key = None  # type: "string"
