from ..factory import Type


class encryptedCredentials(Type):
    # Contains encrypted Telegram Passport data credentials, @data The encrypted credentials
    # @hash The decrypted data hash, @secret Secret for data decryption,
    # encrypted with the service's public key

    data = None  # type: "bytes"
    hash = None  # type: "bytes"
    secret = None  # type: "bytes"
