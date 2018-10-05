from tdwrapper.factory import Method, Type


class publicMessageLink(Type):
    #  a public HTTPS link to a message in a
    #  supergroup or channel @link Message link @html HTML-code for embedding the message

    link = None  # type: "string"
    html = None  # type: "string"


class getPublicMessageLink(Method):
    #  a public HTTPS link to a message. Available only
    #  messages in public supergroups and channels

    chat_id = None  # type: "int53"
    message_id = None  # type: "int53"
    for_album = None  # type: "Bool"
