from ..factory import Type


class passportElementError(Type):
    # Contains the description of an error in a Telegram Passport
    # element @type Type of the Telegram Passport element which has
    # the error @message Error message @source Error source

    type = None  # type: "PassportElementType"
    message = None  # type: "string"
    source = None  # type: "PassportElementErrorSource"
