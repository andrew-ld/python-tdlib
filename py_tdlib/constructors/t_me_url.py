from ..factory import Type


class tMeUrl(Type):
    # Represents a URL linking to an internal Telegram entity @url
    # URL @type Type of the URL

    url = None  # type: "string"
    type = None  # type: "TMeUrlType"
