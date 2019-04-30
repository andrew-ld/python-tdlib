from ..factory import Type


class file(Type):
	id = None  # type: "int32"
	size = None  # type: "int32"
	expected_size = None  # type: "int32"
	local = None  # type: "localFile"
	remote = None  # type: "remoteFile"
