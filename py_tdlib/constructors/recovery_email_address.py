from ..factory import Method, Type


class recoveryEmailAddress(Type):
    # Contains information about the current recovery email address, @recovery_email_address Recovery email address

    recovery_email_address = None  # type: "string"


class getRecoveryEmailAddress(Method):
    # Returns a recovery email address that was previously set up.
    # This method can be used to verify a password provided
    # by the user, @password The password for the current user

    password = None  # type: "string"
