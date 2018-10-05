from ..factory import Method, Type


class publicMessageLink(Type):
    # Contains a public HTTPS link to a message in a
    # public supergroup or channel @link Message link @html HTML-code for embedding the message

    link = None  # type: "string"
    html = None  # type: "string"


class getPublicMessageLink(Method):
    # Returns a public HTTPS link to a message. Available only
    # for messages in public supergroups and channels

    chat_id = None  # type: "int53"
    message_id = None  # type: "int53"
    for_album = None  # type: "Bool"
