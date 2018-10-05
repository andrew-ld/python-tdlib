from ..factory import Type


class authenticationCodeTypeTelegramMessage(Type):
    # An authentication code is delivered via a private Telegram message,
    # which can be viewed in another client, @length Length of the code

    length = None  # type: "int32"


class authenticationCodeTypeSms(Type):
    # An authentication code is delivered via an SMS message to
    # the specified phone number, @length Length of the code

    length = None  # type: "int32"


class authenticationCodeTypeCall(Type):
    # An authentication code is delivered via a phone call to
    # the specified phone number, @length Length of the code

    length = None  # type: "int32"


class authenticationCodeTypeFlashCall(Type):
    # An authentication code is delivered by an immediately cancelled call
    # to the specified phone number. The number from which the
    # call was made is the code, @pattern Pattern of the
    # phone number from which the call will be made

    pattern = None  # type: "string"
