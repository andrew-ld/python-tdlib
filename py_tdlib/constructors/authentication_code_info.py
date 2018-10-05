from ..factory import Method, Type


class authenticationCodeInfo(Type):
    # Information about the authentication code that was sent, @phone_number A
    # phone number that is being authenticated, @type Describes the way
    # the code was sent to the user, @next_type Describes the
    # way the next code will be sent to the user;
    # may be null, @timeout Timeout before the code should be re-sent, in seconds

    phone_number = None  # type: "string"
    type = None  # type: "AuthenticationCodeType"
    next_type = None  # type: "AuthenticationCodeType"
    timeout = None  # type: "int32"


class changePhoneNumber(Method):
    # Changes the phone number of the user and sends an
    # authentication code to the user's new phone number. On success,
    # returns information about the sent code

    phone_number = None  # type: "string"
    allow_flash_call = None  # type: "Bool"
    is_current_phone_number = None  # type: "Bool"


class resendChangePhoneNumberCode(Method):
    # Re-sends the authentication code sent to confirm a new phone
    # number for the user. Works only if the previously received
    # authenticationCodeInfo next_code_type was not null

    pass


class sendPhoneNumberVerificationCode(Method):
    # Sends a code to verify a phone number to be
    # added to a user's Telegram Passport

    phone_number = None  # type: "string"
    allow_flash_call = None  # type: "Bool"
    is_current_phone_number = None  # type: "Bool"


class resendPhoneNumberVerificationCode(Method):
    # Re-sends the code to verify a phone number to be
    # added to a user's Telegram Passport

    pass


class sendPhoneNumberConfirmationCode(Method):
    # Sends phone number confirmation code. Should be called when user
    # presses "https://t.me/confirmphone?phone=*******&hash=**********" or "tg://confirmphone?phone=*******&hash=**********" link, @hash Value of the "hash"
    # parameter from the link

    hash = None  # type: "string"
    phone_number = None  # type: "string"
    allow_flash_call = None  # type: "Bool"
    is_current_phone_number = None  # type: "Bool"


class resendPhoneNumberConfirmationCode(Method):
    # Resends phone number confirmation code

    pass
