from tdwrapper.factory import Type


class encryptedCredentials(Type):
    #  encrypted Telegram Passport data credentials @data The encrypted credentials
    #  The decrypted data hash @secret Secret for data decryption,
    #  with the service's public key

    data = None  # type: "bytes"
    hash = None  # type: "bytes"
    secret = None  # type: "bytes"
