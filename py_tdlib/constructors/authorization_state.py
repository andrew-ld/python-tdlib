from ..factory import Method, Type


class authorizationStateWaitTdlibParameters(Type):
    # TDLib needs TdlibParameters for initialization

    pass


class authorizationStateWaitEncryptionKey(Type):
    # TDLib needs an encryption key to decrypt the local database
    # @is_encrypted True, if the database is currently encrypted

    is_encrypted = None  # type: "Bool"


class authorizationStateWaitPhoneNumber(Type):
    # TDLib needs the user's phone number to authorize

    pass


class authorizationStateWaitCode(Type):
    # TDLib needs the user's authentication code to finalize authorization @is_registered
    # True, if the user is already registered @terms_of_service Telegram terms
    # of service, which should be accepted before user can continue
    # registration; may be null @code_info Information about the authorization code that was sent

    is_registered = None  # type: "Bool"
    terms_of_service = None  # type: "termsOfService"
    code_info = None  # type: "authenticationCodeInfo"


class authorizationStateWaitPassword(Type):
    # The user has been authorized, but needs to enter a
    # password to start using the application @password_hint Hint for the
    # password; can be empty @has_recovery_email_address True if a recovery email
    # address has been set up

    password_hint = None  # type: "string"
    has_recovery_email_address = None  # type: "Bool"
    recovery_email_address_pattern = None  # type: "string"


class authorizationStateReady(Type):
    # The user has been successfully authorized. TDLib is now ready to answer queries

    pass


class authorizationStateLoggingOut(Type):
    # The user is currently logging out

    pass


class authorizationStateClosing(Type):
    # TDLib is closing, all subsequent queries will be answered with
    # the error 500. Note that closing TDLib can take a
    # while. All resources will be freed only after authorizationStateClosed has been received

    pass


class authorizationStateClosed(Type):
    # TDLib client is in its final state. All databases are
    # closed and all resources are released. No other updates will
    # be received after this. All queries will be responded to

    pass


class getAuthorizationState(Method):
    # Returns the current authorization state; this is an offline request.
    # For informational purposes only. Use updateAuthorizationState instead to maintain the current authorization state

    pass
