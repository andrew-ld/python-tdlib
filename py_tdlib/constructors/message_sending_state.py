from ..factory import Type


class messageSendingStatePending(Type):
    # The message is being sent now, but has not yet
    # been delivered to the server

    pass


class messageSendingStateFailed(Type):
    # The message failed to be sent

    pass
