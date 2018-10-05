from ..factory import Method, Type


class accountTtl(Type):
    #  information about the period of inactivity after which the
    #  user's account will automatically be deleted @days Number of
    #  of inactivity before the account will be flagged for
    #  should range from 30-366 days

    days = None  # type: "int32"


class getAccountTtl(Method):
    #  the period of inactivity after which the account of
    #  current user will automatically be deleted

    pass
