from ..factory import Type


class linkStateNone(Type):
    #  phone number of user A is not known to user B

    pass


class linkStateKnowsPhoneNumber(Type):
    #  phone number of user A is known but that
    #  has not been saved to the contacts list of user B

    pass


class linkStateIsContact(Type):
    #  phone number of user A has been saved to
    #  contacts list of user B

    pass
