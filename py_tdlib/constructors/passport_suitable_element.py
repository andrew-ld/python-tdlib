from ..factory import Type


class passportSuitableElement(Type):
	type = None  # type: "PassportElementType"
	is_selfie_required = None  # type: "Bool"
	is_translation_required = None  # type: "Bool"
	is_native_name_required = None  # type: "Bool"
