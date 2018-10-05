from ..factory import Type


class messageForwardedFromUser(Type):
    # The message was originally written by a known user @sender_user_id
    # Identifier of the user that originally sent this message @date
    # Point in time (Unix timestamp) when the message was originally sent

    sender_user_id = None  # type: "int32"
    date = None  # type: "int32"
    forwarded_from_chat_id = None  # type: "int53"
    forwarded_from_message_id = None  # type: "int53"


class messageForwardedPost(Type):
    # The message was originally a post in a channel @chat_id
    # Identifier of the chat from which the message was forwarded
    # @author_signature Post author signature

    chat_id = None  # type: "int53"
    author_signature = None  # type: "string"
    date = None  # type: "int32"
    message_id = None  # type: "int53"
    forwarded_from_chat_id = None  # type: "int53"
    forwarded_from_message_id = None  # type: "int53"
