from ..factory import Method, Type


class formattedText(Type):
    #  text with some entities @text The text @entities Entities
    #  in the text

    text = None  # type: "string"
    entities = None  # type: "vector<textEntity>"


class parseTextEntities(Method):
    #  Bold, Italic, Code, Pre, PreCode and TextUrl entities contained
    #  the text. This is an offline method. Can be
    #  before authorization. Can be called synchronously @text The text
    #  should be parsed @parse_mode Text parse mode

    text = None  # type: "string"
    parse_mode = None  # type: "TextParseMode"
