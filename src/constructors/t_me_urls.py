from ..factory import Method, Type


class tMeUrls(Type):
    #  a list of t.me URLs @urls List of URLs

    urls = None  # type: "vector<tMeUrl>"


class getRecentlyVisitedTMeUrls(Method):
    #  t.me URLs recently visited by a newly registered user
    #  Google Play referrer to identify the user

    referrer = None  # type: "string"
