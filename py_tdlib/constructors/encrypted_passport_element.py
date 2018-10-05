from ..factory import Type


class encryptedPassportElement(Type):
    # Contains information about an encrypted Telegram Passport element; for bots
    # only, @type Type of Telegram Passport element, @data Encrypted JSON-encoded
    # data about the user, @front_side The front side of an
    # identity document, @reverse_side The reverse side of an identity document;
    # may be null, @selfie Selfie with the document; may be
    # null, @translation List of files containing a certified English translation
    # of the document, @files List of attached files, @value Unencrypted
    # data, phone number or email address, @hash Hash of the entire element

    type = None  # type: "PassportElementType"
    data = None  # type: "bytes"
    front_side = None  # type: "datedFile"
    reverse_side = None  # type: "datedFile"
    selfie = None  # type: "datedFile"
    translation = None  # type: "vector<datedFile>"
    files = None  # type: "vector<datedFile>"
    value = None  # type: "string"
    hash = None  # type: "string"
