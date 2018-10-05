from ..factory import Method, Type


class recoveryEmailAddress(Type):
    #  information about the current recovery email address @recovery_email_address Recovery email address

    recovery_email_address = None  # type: "string"


class getRecoveryEmailAddress(Method):
    #  a recovery email address that was previously set up.
    #  method can be used to verify a password provided
    #  the user @password The password for the current user

    password = None  # type: "string"
