from ..factory import Type


class callStatePending(Type):
    # The call is pending, waiting to be accepted by a
    # user @is_created True, if the call has already been created
    # by the server @is_received True, if the call has already
    # been received by the other party

    is_created = None  # type: "Bool"
    is_received = None  # type: "Bool"


class callStateExchangingKeys(Type):
    # The call has been answered and encryption keys are being exchanged

    pass


class callStateReady(Type):
    # The call is ready to use @protocol Call protocols supported
    # by the peer @connections Available UDP reflectors @config A JSON-encoded
    # call config @encryption_key Call encryption key @emojis Encryption key emojis fingerprint

    protocol = None  # type: "callProtocol"
    connections = None  # type: "vector<callConnection>"
    config = None  # type: "string"
    encryption_key = None  # type: "bytes"
    emojis = None  # type: "vector<string>"


class callStateHangingUp(Type):
    # The call is hanging up after discardCall has been called

    pass


class callStateDiscarded(Type):
    # The call has ended successfully @reason The reason, why the
    # call has ended @need_rating True, if the call rating should
    # be sent to the server @need_debug_information True, if the call
    # debug information should be sent to the server

    reason = None  # type: "CallDiscardReason"
    need_rating = None  # type: "Bool"
    need_debug_information = None  # type: "Bool"


class callStateError(Type):
    # The call has ended with an error @error Error. An
    # error with the code 4005000 will be returned if an
    # outgoing call is missed because of an expired timeout

    error = None  # type: "error"
