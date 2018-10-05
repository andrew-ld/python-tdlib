from ..factory import Type


class callDiscardReasonEmpty(Type):
    # The call wasn't discarded, or the reason is unknown

    pass


class callDiscardReasonMissed(Type):
    # The call was ended before the conversation started. It was
    # cancelled by the caller or missed by the other party

    pass


class callDiscardReasonDeclined(Type):
    # The call was ended before the conversation started. It was
    # declined by the other party

    pass


class callDiscardReasonDisconnected(Type):
    # The call was ended during the conversation because the users were disconnected

    pass


class callDiscardReasonHungUp(Type):
    # The call was ended because one of the parties hung up

    pass
