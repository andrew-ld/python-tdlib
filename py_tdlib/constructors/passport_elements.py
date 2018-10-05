from ..factory import Method, Type


class passportElements(Type):
    #  information about saved Telegram Passport elements @elements Telegram Passport

    elements = None  # type: "vector<PassportElement>"


class getAllPassportElements(Method):
    #  all available Telegram Passport elements @password Password of the current user

    password = None  # type: "string"
