from tdwrapper.factory import Method, Type


class userProfilePhotos(Type):
    #  part of the list of user photos @total_count Total
    #  of user profile photos @photos A list of photos

    total_count = None  # type: "int32"
    photos = None  # type: "vector<photo>"


class getUserProfilePhotos(Method):
    #  the profile photos of a user. The result of
    #  query may be outdated: some photos might have been
    #  already @user_id User identifier @offset The number of photos
    #  skip; must be non-negative @limit Maximum number of photos
    #  be returned; up to 100

    user_id = None  # type: "int32"
    offset = None  # type: "int32"
    limit = None  # type: "int32"
