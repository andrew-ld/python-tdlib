from ..factory import Type


class encryptedCredentials(Type):
	data = None  # type: "bytes"
	hash = None  # type: "bytes"
	secret = None  # type: "bytes"
