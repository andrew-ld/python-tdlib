from ..factory import Method, Type


class callbackQueryAnswer(Type):
    # Contains a bot's answer to a callback query, @text Text
    # of the answer, @show_alert True, if an alert should be
    # shown to the user instead of a toast notification, @url
    # URL to be opened

    text = None  # type: "string"
    show_alert = None  # type: "Bool"
    url = None  # type: "string"


class getCallbackQueryAnswer(Method):
    # Sends a callback query to a bot and returns an
    # answer. Returns an error with code 502 if the bot
    # fails to answer the query before the query timeout expires
    # @chat_id Identifier of the chat with the message, @message_id Identifier
    # of the message from which the query originated, @payload Query payload

    chat_id = None  # type: "int53"
    message_id = None  # type: "int53"
    payload = None  # type: "CallbackQueryPayload"
