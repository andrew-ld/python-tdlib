from ..factory import Type


class secretChatStatePending(Type):
    # The secret chat is not yet created; waiting for the
    # other user to get online

    pass


class secretChatStateReady(Type):
    # The secret chat is ready to use

    pass


class secretChatStateClosed(Type):
    # The secret chat is closed

    pass
