from tdwrapper.factory import Type


class textEntityTypeMention(Type):
    #  mention of a user by their username

    pass


class textEntityTypeHashtag(Type):
    #  hashtag text, beginning with "#"

    pass


class textEntityTypeCashtag(Type):
    #  cashtag text, beginning with "$" and consisting of capital
    #  letters (i.e. "$USD")

    pass


class textEntityTypeBotCommand(Type):
    #  bot command, beginning with "/". This shouldn't be highlighted
    #  there are no bots in the chat

    pass


class textEntityTypeUrl(Type):
    #  HTTP URL

    pass


class textEntityTypeEmailAddress(Type):
    #  email address

    pass


class textEntityTypeBold(Type):
    #  bold text

    pass


class textEntityTypeItalic(Type):
    #  italic text

    pass


class textEntityTypeCode(Type):
    #  that must be formatted as if inside a code HTML tag

    pass


class textEntityTypePre(Type):
    #  that must be formatted as if inside a pre HTML tag

    pass


class textEntityTypePreCode(Type):
    #  that must be formatted as if inside pre, and
    #  HTML tags @language Programming language of the code; as
    #  by the sender

    language = None  # type: "string"


class textEntityTypeTextUrl(Type):
    #  text description shown instead of a raw URL @url
    #  or tg:// URL to be opened when the link is clicked

    url = None  # type: "string"


class textEntityTypeMentionName(Type):
    #  text shows instead of a raw mention of the
    #  (e.g., when the user has no username) @user_id Identifier
    #  the mentioned user

    user_id = None  # type: "int32"


class textEntityTypePhoneNumber(Type):
    #  phone number

    pass
