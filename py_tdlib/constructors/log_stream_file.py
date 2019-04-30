from ..factory import Type


class logStreamFile(Type):
	path = None  # type: "string"
	max_file_size = None  # type: "int53"
