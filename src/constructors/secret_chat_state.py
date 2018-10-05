from ..factory import Type


class secretChatStatePending(Type):
    #  secret chat is not yet created; waiting for the
    #  user to get online

    pass


class secretChatStateReady(Type):
    #  secret chat is ready to use

    pass


class secretChatStateClosed(Type):
    #  secret chat is closed

    pass
