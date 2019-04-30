from ..factory import Type


class updateFileGenerationStart(Type):
	generation_id = None  # type: "int64"
	original_path = None  # type: "string"
	destination_path = None  # type: "string"
	conversion = None  # type: "string"
