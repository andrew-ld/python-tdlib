from tdwrapper.factory import Type


class replyMarkupRemoveKeyboard(Type):
    #  clients to remove the keyboard once this message has
    #  received. This kind of keyboard can't be received in
    #  incoming message; instead, UpdateChatReplyMarkup with message_id == 0 will be sent

    is_personal = None  # type: "Bool"


class replyMarkupForceReply(Type):
    #  clients to force a reply to this message

    is_personal = None  # type: "Bool"


class replyMarkupShowKeyboard(Type):
    #  a custom keyboard layout to quickly reply to bots

    rows = None  # type: "vector<vector<keyboardButton>>"
    resize_keyboard = None  # type: "Bool"
    one_time = None  # type: "Bool"
    is_personal = None  # type: "Bool"


class replyMarkupInlineKeyboard(Type):
    #  an inline keyboard layout

    rows = None  # type: "vector<vector<inlineKeyboardButton>>"
