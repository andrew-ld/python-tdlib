from ..factory import Method, Type


class textEntities(Type):
    #  a list of text entities @entities List of text

    entities = None  # type: "vector<textEntity>"


class getTextEntities(Method):
    #  all entities (mentions, hashtags, cashtags, bot commands, URLs, and
    #  addresses) contained in the text. This is an offline
    #  Can be called before authorization. Can be called synchronously
    #  The text in which to look for entites

    text = None  # type: "string"
