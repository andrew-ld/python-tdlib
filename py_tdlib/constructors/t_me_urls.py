from ..factory import Method, Type


class tMeUrls(Type):
    # Contains a list of t.me URLs @urls List of URLs

    urls = None  # type: "vector<tMeUrl>"


class getRecentlyVisitedTMeUrls(Method):
    # Returns t.me URLs recently visited by a newly registered user
    # @referrer Google Play referrer to identify the user

    referrer = None  # type: "string"
