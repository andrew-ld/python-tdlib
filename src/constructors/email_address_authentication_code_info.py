from tdwrapper.factory import Method, Type


class emailAddressAuthenticationCodeInfo(Type):
    #  about the email address authentication code that was sent
    #  Pattern of the email address to which an authentication
    #  was sent @length Length of the code; 0 if

    email_address_pattern = None  # type: "string"
    length = None  # type: "int32"


class requestPasswordRecovery(Method):
    #  to send a password recovery code to an email
    #  that was previously set up

    pass


class sendEmailAddressVerificationCode(Method):
    #  a code to verify an email address to be
    #  to a user's Telegram Passport @email_address Email address

    email_address = None  # type: "string"


class resendEmailAddressVerificationCode(Method):
    #  the code to verify an email address to be
    #  to a user's Telegram Passport

    pass
