from tdwrapper.factory import Type


class tMeUrl(Type):
    #  a URL linking to an internal Telegram entity @url
    #  @type Type of the URL

    url = None  # type: "string"
    type = None  # type: "TMeUrlType"
