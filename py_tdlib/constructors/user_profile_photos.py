from ..factory import Type


class userProfilePhotos(Type):
	total_count = None  # type: "int32"
	photos = None  # type: "vector<userProfilePhoto>"
