from tdwrapper.factory import Type


class draftMessage(Type):
    #  information about a message draft @reply_to_message_id Identifier of the
    #  to reply to; 0 if none @input_message_text Content of
    #  message draft; this should always be of type inputMessageText

    reply_to_message_id = None  # type: "int53"
    input_message_text = None  # type: "InputMessageContent"
