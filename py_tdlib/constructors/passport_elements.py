from ..factory import Method, Type


class passportElements(Type):
    # Contains information about saved Telegram Passport elements @elements Telegram Passport elements

    elements = None  # type: "vector<PassportElement>"


class getAllPassportElements(Method):
    # Returns all available Telegram Passport elements @password Password of the current user

    password = None  # type: "string"
