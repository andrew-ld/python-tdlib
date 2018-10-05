from ..factory import Method, Type


class formattedText(Type):
    # A text with some entities @text The text @entities Entities
    # contained in the text

    text = None  # type: "string"
    entities = None  # type: "vector<textEntity>"


class parseTextEntities(Method):
    # Parses Bold, Italic, Code, Pre, PreCode and TextUrl entities contained
    # in the text. This is an offline method. Can be
    # called before authorization. Can be called synchronously @text The text
    # which should be parsed @parse_mode Text parse mode

    text = None  # type: "string"
    parse_mode = None  # type: "TextParseMode"
