from ..factory import Type


class replyMarkupRemoveKeyboard(Type):
    # Instructs clients to remove the keyboard once this message has
    # been received. This kind of keyboard can't be received in
    # an incoming message; instead, UpdateChatReplyMarkup with message_id == 0 will be sent

    is_personal = None  # type: "Bool"


class replyMarkupForceReply(Type):
    # Instructs clients to force a reply to this message

    is_personal = None  # type: "Bool"


class replyMarkupShowKeyboard(Type):
    # Contains a custom keyboard layout to quickly reply to bots

    rows = None  # type: "vector<vector<keyboardButton>>"
    resize_keyboard = None  # type: "Bool"
    one_time = None  # type: "Bool"
    is_personal = None  # type: "Bool"


class replyMarkupInlineKeyboard(Type):
    # Contains an inline keyboard layout

    rows = None  # type: "vector<vector<inlineKeyboardButton>>"
