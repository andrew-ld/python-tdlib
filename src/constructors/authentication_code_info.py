from tdwrapper.factory import Method, Type


class authenticationCodeInfo(Type):
    #  about the authentication code that was sent @phone_number A
    #  number that is being authenticated @type Describes the way
    #  code was sent to the user @next_type Describes the
    #  the next code will be sent to the user;
    #  be null @timeout Timeout before the code should be re-sent, in seconds

    phone_number = None  # type: "string"
    type = None  # type: "AuthenticationCodeType"
    next_type = None  # type: "AuthenticationCodeType"
    timeout = None  # type: "int32"


class changePhoneNumber(Method):
    #  the phone number of the user and sends an
    #  code to the user's new phone number. On success,
    #  information about the sent code

    phone_number = None  # type: "string"
    allow_flash_call = None  # type: "Bool"
    is_current_phone_number = None  # type: "Bool"


class resendChangePhoneNumberCode(Method):
    #  the authentication code sent to confirm a new phone
    #  for the user. Works only if the previously received
    #  next_code_type was not null

    pass


class sendPhoneNumberVerificationCode(Method):
    #  a code to verify a phone number to be
    #  to a user's Telegram Passport

    phone_number = None  # type: "string"
    allow_flash_call = None  # type: "Bool"
    is_current_phone_number = None  # type: "Bool"


class resendPhoneNumberVerificationCode(Method):
    #  the code to verify a phone number to be
    #  to a user's Telegram Passport

    pass


class sendPhoneNumberConfirmationCode(Method):
    #  phone number confirmation code. Should be called when user
    #  "https://t.me/confirmphone?phone=*******&hash=**********" or "tg://confirmphone?phone=*******&hash=**********" link @hash Value of the "hash"
    #  from the link

    hash = None  # type: "string"
    phone_number = None  # type: "string"
    allow_flash_call = None  # type: "Bool"
    is_current_phone_number = None  # type: "Bool"


class resendPhoneNumberConfirmationCode(Method):
    #  phone number confirmation code

    pass
