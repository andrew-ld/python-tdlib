from ..factory import Type


class draftMessage(Type):
    # Contains information about a message draft, @reply_to_message_id Identifier of the
    # message to reply to; 0 if none, @input_message_text Content of
    # the message draft; this should always be of type inputMessageText

    reply_to_message_id = None  # type: "int53"
    input_message_text = None  # type: "InputMessageContent"
