from ..factory import Type


class inlineKeyboardButtonTypeUrl(Type):
    # A button that opens a specified URL, @url HTTP or
    # tg:// URL to open

    url = None  # type: "string"


class inlineKeyboardButtonTypeCallback(Type):
    # A button that sends a special callback query to a
    # bot, @data Data to be sent to the bot via a callback query

    data = None  # type: "bytes"


class inlineKeyboardButtonTypeCallbackGame(Type):
    # A button with a game that sends a special callback
    # query to a bot. This button must be in the
    # first column and row of the keyboard and can be
    # attached only to a message with content of the type messageGame

    pass


class inlineKeyboardButtonTypeSwitchInline(Type):
    # A button that forces an inline query to the bot
    # to be inserted in the input field, @query Inline query
    # to be sent to the bot, @in_current_chat True, if the
    # inline query should be sent from the current chat

    query = None  # type: "string"
    in_current_chat = None  # type: "Bool"


class inlineKeyboardButtonTypeBuy(Type):
    # A button to buy something. This button must be in
    # the first column and row of the keyboard and can
    # be attached only to a message with content of the type messageInvoice

    pass
