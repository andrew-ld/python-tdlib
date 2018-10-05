from ..factory import Method, Type


class accountTtl(Type):
    # Contains information about the period of inactivity after which the
    # current user's account will automatically be deleted @days Number of
    # days of inactivity before the account will be flagged for
    # deletion; should range from 30-366 days

    days = None  # type: "int32"


class getAccountTtl(Method):
    # Returns the period of inactivity after which the account of
    # the current user will automatically be deleted

    pass
