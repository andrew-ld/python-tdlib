from tdwrapper.factory import Type


class inputPassportElementErrorSourceUnspecified(Type):
    #  element contains an error in an unspecified place. The
    #  will be considered resolved when new data is added
    #  Current hash of the entire element

    element_hash = None  # type: "bytes"


class inputPassportElementErrorSourceDataField(Type):
    #  data field contains an error. The error is considered
    #  when the field's value changes @field_name Field name @data_hash Current data hash

    field_name = None  # type: "string"
    data_hash = None  # type: "bytes"


class inputPassportElementErrorSourceFrontSide(Type):
    #  front side of the document contains an error. The
    #  is considered resolved when the file with the front
    #  of the document changes @file_hash Current hash of the
    #  containing the front side

    file_hash = None  # type: "bytes"


class inputPassportElementErrorSourceReverseSide(Type):
    #  reverse side of the document contains an error. The
    #  is considered resolved when the file with the reverse
    #  of the document changes @file_hash Current hash of the
    #  containing the reverse side

    file_hash = None  # type: "bytes"


class inputPassportElementErrorSourceSelfie(Type):
    #  selfie contains an error. The error is considered resolved
    #  the file with the selfie changes @file_hash Current hash
    #  the file containing the selfie

    file_hash = None  # type: "bytes"


class inputPassportElementErrorSourceTranslationFile(Type):
    #  of the files containing the translation of the document
    #  an error. The error is considered resolved when the
    #  with the translation changes @file_hash Current hash of the
    #  containing the translation

    file_hash = None  # type: "bytes"


class inputPassportElementErrorSourceTranslationFiles(Type):
    #  translation of the document contains an error. The error
    #  considered resolved when the list of files changes @file_hashes
    #  hashes of all files with the translation

    file_hashes = None  # type: "vector<bytes>"


class inputPassportElementErrorSourceFile(Type):
    #  file contains an error. The error is considered resolved
    #  the file changes @file_hash Current hash of the file
    #  has the error

    file_hash = None  # type: "bytes"


class inputPassportElementErrorSourceFiles(Type):
    #  list of attached files contains an error. The error
    #  considered resolved when the file list changes @file_hashes Current
    #  of all attached files

    file_hashes = None  # type: "vector<bytes>"
