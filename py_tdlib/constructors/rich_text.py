from ..factory import Type


class richTextPlain(Type):
    #  plain text @text Text

    text = None  # type: "string"


class richTextBold(Type):
    #  bold rich text @text Text

    text = None  # type: "RichText"


class richTextItalic(Type):
    #  italicized rich text @text Text

    text = None  # type: "RichText"


class richTextUnderline(Type):
    #  underlined rich text @text Text

    text = None  # type: "RichText"


class richTextStrikethrough(Type):
    #  strike-through rich text @text Text

    text = None  # type: "RichText"


class richTextFixed(Type):
    #  fixed-width rich text @text Text

    text = None  # type: "RichText"


class richTextUrl(Type):
    #  rich text URL link @text Text @url URL

    text = None  # type: "RichText"
    url = None  # type: "string"


class richTextEmailAddress(Type):
    #  rich text email link @text Text @email_address Email address

    text = None  # type: "RichText"
    email_address = None  # type: "string"


class richTexts(Type):
    #  concatenation of rich texts @texts Texts

    texts = None  # type: "vector<RichText>"
