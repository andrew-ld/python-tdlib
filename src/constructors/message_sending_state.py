from tdwrapper.factory import Type


class messageSendingStatePending(Type):
    #  message is being sent now, but has not yet
    #  delivered to the server

    pass


class messageSendingStateFailed(Type):
    #  message failed to be sent

    pass
