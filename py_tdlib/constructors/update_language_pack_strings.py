from ..factory import Type


class updateLanguagePackStrings(Type):
	localization_target = None  # type: "string"
	language_pack_id = None  # type: "string"
	strings = None  # type: "vector<languagePackString>"
