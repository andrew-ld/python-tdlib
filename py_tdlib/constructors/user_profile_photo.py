from ..factory import Type


class userProfilePhoto(Type):
	id = None  # type: "int64"
	added_date = None  # type: "int32"
	sizes = None  # type: "vector<photoSize>"
