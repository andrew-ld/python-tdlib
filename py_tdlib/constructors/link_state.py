from ..factory import Type


class linkStateNone(Type):
    # The phone number of user A is not known to user B

    pass


class linkStateKnowsPhoneNumber(Type):
    # The phone number of user A is known but that
    # number has not been saved to the contacts list of user B

    pass


class linkStateIsContact(Type):
    # The phone number of user A has been saved to
    # the contacts list of user B

    pass
