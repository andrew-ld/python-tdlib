from ..factory import Method, Type


class passportAuthorizationForm(Type):
    #  information about a Telegram Passport authorization form that was
    #  @id Unique identifier of the authorization form

    id = None  # type: "int32"
    required_elements = None  # type: "vector<passportRequiredElement>"
    elements = None  # type: "vector<PassportElement>"
    errors = None  # type: "vector<passportElementError>"
    privacy_policy_url = None  # type: "string"


class getPassportAuthorizationForm(Method):
    #  a Telegram Passport authorization form for sharing data with
    #  service @bot_user_id User identifier of the service's bot @scope
    #  Passport element types requested by the service @public_key Service's
    #  @nonce Authorization form nonce provided by the service @password
    #  of the current user

    bot_user_id = None  # type: "int32"
    scope = None  # type: "string"
    public_key = None  # type: "string"
    nonce = None  # type: "string"
    password = None  # type: "string"
