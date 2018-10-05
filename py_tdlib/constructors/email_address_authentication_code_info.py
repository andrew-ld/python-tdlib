from ..factory import Method, Type


class emailAddressAuthenticationCodeInfo(Type):
    # Information about the email address authentication code that was sent
    # @email_address_pattern Pattern of the email address to which an authentication
    # code was sent, @length Length of the code; 0 if unknown

    email_address_pattern = None  # type: "string"
    length = None  # type: "int32"


class requestPasswordRecovery(Method):
    # Requests to send a password recovery code to an email
    # address that was previously set up

    pass


class sendEmailAddressVerificationCode(Method):
    # Sends a code to verify an email address to be
    # added to a user's Telegram Passport, @email_address Email address

    email_address = None  # type: "string"


class resendEmailAddressVerificationCode(Method):
    # Re-sends the code to verify an email address to be
    # added to a user's Telegram Passport

    pass
