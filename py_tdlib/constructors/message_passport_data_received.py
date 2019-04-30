from ..factory import Type


class messagePassportDataReceived(Type):
	elements = None  # type: "vector<encryptedPassportElement>"
	credentials = None  # type: "encryptedCredentials"
