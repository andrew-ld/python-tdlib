from ..factory import Type


class inputPassportElementError(Type):
    # Contains the description of an error in a Telegram Passport
    # element; for bots only @type Type of Telegram Passport element
    # that has the error @message Error message @source Error source

    type = None  # type: "PassportElementType"
    message = None  # type: "string"
    source = None  # type: "InputPassportElementErrorSource"
