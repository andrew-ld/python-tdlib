from ..factory import Type


class authenticationCodeTypeTelegramMessage(Type):
    #  authentication code is delivered via a private Telegram message,
    #  can be viewed in another client @length Length of the code

    length = None  # type: "int32"


class authenticationCodeTypeSms(Type):
    #  authentication code is delivered via an SMS message to
    #  specified phone number @length Length of the code

    length = None  # type: "int32"


class authenticationCodeTypeCall(Type):
    #  authentication code is delivered via a phone call to
    #  specified phone number @length Length of the code

    length = None  # type: "int32"


class authenticationCodeTypeFlashCall(Type):
    #  authentication code is delivered by an immediately cancelled call
    #  the specified phone number. The number from which the
    #  was made is the code @pattern Pattern of the
    #  number from which the call will be made

    pattern = None  # type: "string"
