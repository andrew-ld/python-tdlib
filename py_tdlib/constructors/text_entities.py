from ..factory import Method, Type


class textEntities(Type):
    # Contains a list of text entities @entities List of text entities

    entities = None  # type: "vector<textEntity>"


class getTextEntities(Method):
    # Returns all entities (mentions, hashtags, cashtags, bot commands, URLs, and
    # email addresses) contained in the text. This is an offline
    # method. Can be called before authorization. Can be called synchronously
    # @text The text in which to look for entites

    text = None  # type: "string"
