from ..factory import Type


class inputCredentialsSaved(Type):
    # Applies if a user chooses some previously saved payment credentials.
    # To use their previously saved credentials, the user must have
    # a valid temporary password, @saved_credentials_id Identifier of the saved credentials

    saved_credentials_id = None  # type: "string"


class inputCredentialsNew(Type):
    # Applies if a user enters new credentials on a payment
    # provider website, @data Contains JSON-encoded data with a credential identifier
    # from the payment provider, @allow_save True, if the credential identifier
    # can be saved on the server side

    data = None  # type: "string"
    allow_save = None  # type: "Bool"


class inputCredentialsAndroidPay(Type):
    # Applies if a user enters new credentials using Android Pay
    # @data JSON-encoded data with the credential identifier

    data = None  # type: "string"


class inputCredentialsApplePay(Type):
    # Applies if a user enters new credentials using Apple Pay
    # @data JSON-encoded data with the credential identifier

    data = None  # type: "string"
