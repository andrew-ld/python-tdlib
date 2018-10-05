from tdwrapper.factory import Type


class callDiscardReasonEmpty(Type):
    #  call wasn't discarded, or the reason is unknown

    pass


class callDiscardReasonMissed(Type):
    #  call was ended before the conversation started. It was
    #  by the caller or missed by the other party

    pass


class callDiscardReasonDeclined(Type):
    #  call was ended before the conversation started. It was
    #  by the other party

    pass


class callDiscardReasonDisconnected(Type):
    #  call was ended during the conversation because the users were disconnected

    pass


class callDiscardReasonHungUp(Type):
    #  call was ended because one of the parties hung

    pass
