from ..factory import Type


class passportRequiredElement(Type):
    #  a description of the required Telegram Passport element that
    #  requested by a service @suitable_elements List of Telegram Passport
    #  any of which is enough to provide

    suitable_elements = None  # type: "vector<passportSuitableElement>"
