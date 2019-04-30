from ..factory import Type


class languagePackInfo(Type):
	id = None  # type: "string"
	base_language_pack_id = None  # type: "string"
	name = None  # type: "string"
	native_name = None  # type: "string"
	plural_code = None  # type: "string"
	is_official = None  # type: "Bool"
	is_rtl = None  # type: "Bool"
	is_beta = None  # type: "Bool"
	is_installed = None  # type: "Bool"
	total_string_count = None  # type: "int32"
	translated_string_count = None  # type: "int32"
	local_string_count = None  # type: "int32"
	translation_url = None  # type: "string"
