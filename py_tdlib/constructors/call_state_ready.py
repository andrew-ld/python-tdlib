from ..factory import Type


class callStateReady(Type):
	protocol = None  # type: "callProtocol"
	connections = None  # type: "vector<callConnection>"
	config = None  # type: "string"
	encryption_key = None  # type: "bytes"
	emojis = None  # type: "vector<string>"
	allow_p2p = None  # type: "Bool"
