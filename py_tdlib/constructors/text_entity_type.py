from ..factory import Type


class textEntityTypeMention(Type):
    # A mention of a user by their username

    pass


class textEntityTypeHashtag(Type):
    # A hashtag text, beginning with "#"

    pass


class textEntityTypeCashtag(Type):
    # A cashtag text, beginning with "$" and consisting of capital
    # english letters (i.e. "$USD")

    pass


class textEntityTypeBotCommand(Type):
    # A bot command, beginning with "/". This shouldn't be highlighted
    # if there are no bots in the chat

    pass


class textEntityTypeUrl(Type):
    # An HTTP URL

    pass


class textEntityTypeEmailAddress(Type):
    # An email address

    pass


class textEntityTypeBold(Type):
    # A bold text

    pass


class textEntityTypeItalic(Type):
    # An italic text

    pass


class textEntityTypeCode(Type):
    # Text that must be formatted as if inside a code HTML tag

    pass


class textEntityTypePre(Type):
    # Text that must be formatted as if inside a pre HTML tag

    pass


class textEntityTypePreCode(Type):
    # Text that must be formatted as if inside pre, and
    # code HTML tags @language Programming language of the code; as
    # defined by the sender

    language = None  # type: "string"


class textEntityTypeTextUrl(Type):
    # A text description shown instead of a raw URL @url
    # HTTP or tg:// URL to be opened when the link is clicked

    url = None  # type: "string"


class textEntityTypeMentionName(Type):
    # A text shows instead of a raw mention of the
    # user (e.g., when the user has no username) @user_id Identifier
    # of the mentioned user

    user_id = None  # type: "int32"


class textEntityTypePhoneNumber(Type):
    # A phone number

    pass
