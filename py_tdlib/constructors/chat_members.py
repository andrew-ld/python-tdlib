from ..factory import Type


class chatMembers(Type):
	total_count = None  # type: "int32"
	members = None  # type: "vector<chatMember>"
