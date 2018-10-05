from ..factory import Method, Type


class passwordState(Type):
    # Represents the current state of 2-step verification @has_password True if
    # a 2-step verification password is set @password_hint Hint for the
    # password; can be empty @has_recovery_email_address True if a recovery email
    # is set @has_passport_data True if some Telegram Passport elements were
    # saved @unconfirmed_recovery_email_address_pattern Pattern of the email address to which the
    # confirmation email was sent

    has_password = None  # type: "Bool"
    password_hint = None  # type: "string"
    has_recovery_email_address = None  # type: "Bool"
    has_passport_data = None  # type: "Bool"
    unconfirmed_recovery_email_address_pattern = None  # type: "string"


class getPasswordState(Method):
    # Returns the current state of 2-step verification

    pass


class setPassword(Method):
    # Changes the password for the user. If a new recovery
    # email address is specified, then the error EMAIL_UNCONFIRMED is returned
    # and the password change will not be applied until the
    # new recovery email address has been confirmed. The application should
    # periodically call getPasswordState to check whether the new email address has been confirmed

    old_password = None  # type: "string"
    new_password = None  # type: "string"
    new_hint = None  # type: "string"
    set_recovery_email_address = None  # type: "Bool"
    new_recovery_email_address = None  # type: "string"


class setRecoveryEmailAddress(Method):
    # Changes the recovery email address of the user. If a
    # new recovery email address is specified, then the error EMAIL_UNCONFIRMED
    # is returned and the email address will not be changed
    # until the new email has been confirmed. The application should
    # periodically call getPasswordState to check whether the email address has been confirmed.

    password = None  # type: "string"
    new_recovery_email_address = None  # type: "string"


class recoverPassword(Method):
    # Recovers the password using a recovery code sent to an
    # email address that was previously set up @recovery_code Recovery code to check

    recovery_code = None  # type: "string"
