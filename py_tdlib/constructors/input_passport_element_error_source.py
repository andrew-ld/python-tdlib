from ..factory import Type


class inputPassportElementErrorSourceUnspecified(Type):
    # The element contains an error in an unspecified place. The
    # error will be considered resolved when new data is added
    # @element_hash Current hash of the entire element

    element_hash = None  # type: "bytes"


class inputPassportElementErrorSourceDataField(Type):
    # A data field contains an error. The error is considered
    # resolved when the field's value changes @field_name Field name @data_hash Current data hash

    field_name = None  # type: "string"
    data_hash = None  # type: "bytes"


class inputPassportElementErrorSourceFrontSide(Type):
    # The front side of the document contains an error. The
    # error is considered resolved when the file with the front
    # side of the document changes @file_hash Current hash of the
    # file containing the front side

    file_hash = None  # type: "bytes"


class inputPassportElementErrorSourceReverseSide(Type):
    # The reverse side of the document contains an error. The
    # error is considered resolved when the file with the reverse
    # side of the document changes @file_hash Current hash of the
    # file containing the reverse side

    file_hash = None  # type: "bytes"


class inputPassportElementErrorSourceSelfie(Type):
    # The selfie contains an error. The error is considered resolved
    # when the file with the selfie changes @file_hash Current hash
    # of the file containing the selfie

    file_hash = None  # type: "bytes"


class inputPassportElementErrorSourceTranslationFile(Type):
    # One of the files containing the translation of the document
    # contains an error. The error is considered resolved when the
    # file with the translation changes @file_hash Current hash of the
    # file containing the translation

    file_hash = None  # type: "bytes"


class inputPassportElementErrorSourceTranslationFiles(Type):
    # The translation of the document contains an error. The error
    # is considered resolved when the list of files changes @file_hashes
    # Current hashes of all files with the translation

    file_hashes = None  # type: "vector<bytes>"


class inputPassportElementErrorSourceFile(Type):
    # The file contains an error. The error is considered resolved
    # when the file changes @file_hash Current hash of the file
    # which has the error

    file_hash = None  # type: "bytes"


class inputPassportElementErrorSourceFiles(Type):
    # The list of attached files contains an error. The error
    # is considered resolved when the file list changes @file_hashes Current
    # hashes of all attached files

    file_hashes = None  # type: "vector<bytes>"
