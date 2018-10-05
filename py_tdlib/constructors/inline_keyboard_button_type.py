from ..factory import Type


class inlineKeyboardButtonTypeUrl(Type):
    #  button that opens a specified URL @url HTTP or
    #  URL to open

    url = None  # type: "string"


class inlineKeyboardButtonTypeCallback(Type):
    #  button that sends a special callback query to a
    #  @data Data to be sent to the bot via a callback query

    data = None  # type: "bytes"


class inlineKeyboardButtonTypeCallbackGame(Type):
    #  button with a game that sends a special callback
    #  to a bot. This button must be in the
    #  column and row of the keyboard and can be
    #  only to a message with content of the type

    pass


class inlineKeyboardButtonTypeSwitchInline(Type):
    #  button that forces an inline query to the bot
    #  be inserted in the input field @query Inline query
    #  be sent to the bot @in_current_chat True, if the
    #  query should be sent from the current chat

    query = None  # type: "string"
    in_current_chat = None  # type: "Bool"


class inlineKeyboardButtonTypeBuy(Type):
    #  button to buy something. This button must be in
    #  first column and row of the keyboard and can
    #  attached only to a message with content of the type messageInvoice

    pass
