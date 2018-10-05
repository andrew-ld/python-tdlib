from tdwrapper.factory import Type


class passportElementError(Type):
    #  the description of an error in a Telegram Passport
    #  @type Type of the Telegram Passport element which has
    #  error @message Error message @source Error source

    type = None  # type: "PassportElementType"
    message = None  # type: "string"
    source = None  # type: "PassportElementErrorSource"
