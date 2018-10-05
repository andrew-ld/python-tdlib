from tdwrapper.factory import Method, Type


class hashtags(Type):
    #  a list of hashtags @hashtags A list of hashtags

    hashtags = None  # type: "vector<string>"


class searchHashtags(Method):
    #  for recently used hashtags by their prefix @prefix Hashtag
    #  to search for @limit Maximum number of hashtags to be returned

    prefix = None  # type: "string"
    limit = None  # type: "int32"
