from tdwrapper.factory import Type


class encryptedPassportElement(Type):
    #  information about an encrypted Telegram Passport element; for bots
    #  @type Type of Telegram Passport element @data Encrypted JSON-encoded
    #  about the user @front_side The front side of an
    #  document @reverse_side The reverse side of an identity document;
    #  be null @selfie Selfie with the document; may be
    #  @translation List of files containing a certified English translation
    #  the document @files List of attached files @value Unencrypted
    #  phone number or email address @hash Hash of the entire element

    type = None  # type: "PassportElementType"
    data = None  # type: "bytes"
    front_side = None  # type: "datedFile"
    reverse_side = None  # type: "datedFile"
    selfie = None  # type: "datedFile"
    translation = None  # type: "vector<datedFile>"
    files = None  # type: "vector<datedFile>"
    value = None  # type: "string"
    hash = None  # type: "string"
