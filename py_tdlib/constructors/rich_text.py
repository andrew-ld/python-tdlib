from ..factory import Type


class richTextPlain(Type):
    # A plain text, @text Text

    text = None  # type: "string"


class richTextBold(Type):
    # A bold rich text, @text Text

    text = None  # type: "RichText"


class richTextItalic(Type):
    # An italicized rich text, @text Text

    text = None  # type: "RichText"


class richTextUnderline(Type):
    # An underlined rich text, @text Text

    text = None  # type: "RichText"


class richTextStrikethrough(Type):
    # A strike-through rich text, @text Text

    text = None  # type: "RichText"


class richTextFixed(Type):
    # A fixed-width rich text, @text Text

    text = None  # type: "RichText"


class richTextUrl(Type):
    # A rich text URL link, @text Text, @url URL

    text = None  # type: "RichText"
    url = None  # type: "string"


class richTextEmailAddress(Type):
    # A rich text email link, @text Text, @email_address Email address

    text = None  # type: "RichText"
    email_address = None  # type: "string"


class richTexts(Type):
    # A concatenation of rich texts, @texts Texts

    texts = None  # type: "vector<RichText>"
