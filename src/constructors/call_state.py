from ..factory import Type


class callStatePending(Type):
    #  call is pending, waiting to be accepted by a
    #  @is_created True, if the call has already been created
    #  the server @is_received True, if the call has already
    #  received by the other party

    is_created = None  # type: "Bool"
    is_received = None  # type: "Bool"


class callStateExchangingKeys(Type):
    #  call has been answered and encryption keys are being

    pass


class callStateReady(Type):
    #  call is ready to use @protocol Call protocols supported
    #  the peer @connections Available UDP reflectors @config A JSON-encoded
    #  config @encryption_key Call encryption key @emojis Encryption key emojis

    protocol = None  # type: "callProtocol"
    connections = None  # type: "vector<callConnection>"
    config = None  # type: "string"
    encryption_key = None  # type: "bytes"
    emojis = None  # type: "vector<string>"


class callStateHangingUp(Type):
    #  call is hanging up after discardCall has been called

    pass


class callStateDiscarded(Type):
    #  call has ended successfully @reason The reason, why the
    #  has ended @need_rating True, if the call rating should
    #  sent to the server @need_debug_information True, if the call
    #  information should be sent to the server

    reason = None  # type: "CallDiscardReason"
    need_rating = None  # type: "Bool"
    need_debug_information = None  # type: "Bool"


class callStateError(Type):
    #  call has ended with an error @error Error. An
    #  with the code 4005000 will be returned if an
    #  call is missed because of an expired timeout

    error = None  # type: "error"
