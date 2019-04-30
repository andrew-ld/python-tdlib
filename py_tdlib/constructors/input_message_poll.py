from ..factory import Type


class inputMessagePoll(Type):
	question = None  # type: "string"
	options = None  # type: "vector<string>"
