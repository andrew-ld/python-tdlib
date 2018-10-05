from tdwrapper.factory import Type


class inputCredentialsSaved(Type):
    #  if a user chooses some previously saved payment credentials.
    #  use their previously saved credentials, the user must have
    #  valid temporary password @saved_credentials_id Identifier of the saved credentials

    saved_credentials_id = None  # type: "string"


class inputCredentialsNew(Type):
    #  if a user enters new credentials on a payment
    #  website @data Contains JSON-encoded data with a credential identifier
    #  the payment provider @allow_save True, if the credential identifier
    #  be saved on the server side

    data = None  # type: "string"
    allow_save = None  # type: "Bool"


class inputCredentialsAndroidPay(Type):
    #  if a user enters new credentials using Android Pay
    #  JSON-encoded data with the credential identifier

    data = None  # type: "string"


class inputCredentialsApplePay(Type):
    #  if a user enters new credentials using Apple Pay
    #  JSON-encoded data with the credential identifier

    data = None  # type: "string"
