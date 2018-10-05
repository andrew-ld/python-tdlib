from ..factory import Method, Type


class callbackQueryAnswer(Type):
    #  a bot's answer to a callback query @text Text
    #  the answer @show_alert True, if an alert should be
    #  to the user instead of a toast notification @url
    #  to be opened

    text = None  # type: "string"
    show_alert = None  # type: "Bool"
    url = None  # type: "string"


class getCallbackQueryAnswer(Method):
    #  a callback query to a bot and returns an
    #  Returns an error with code 502 if the bot
    #  to answer the query before the query timeout expires
    #  Identifier of the chat with the message @message_id Identifier
    #  the message from which the query originated @payload Query

    chat_id = None  # type: "int53"
    message_id = None  # type: "int53"
    payload = None  # type: "CallbackQueryPayload"
