from ..factory import Type


class passportElementErrorSourceUnspecified(Type):
    # The element contains an error in an unspecified place. The
    # error will be considered resolved when new data is added

    pass


class passportElementErrorSourceDataField(Type):
    # One of the data fields contains an error. The error
    # will be considered resolved when the value of the field
    # changes @field_name Field name

    field_name = None  # type: "string"


class passportElementErrorSourceFrontSide(Type):
    # The front side of the document contains an error. The
    # error will be considered resolved when the file with the front side changes

    pass


class passportElementErrorSourceReverseSide(Type):
    # The reverse side of the document contains an error. The
    # error will be considered resolved when the file with the reverse side changes

    pass


class passportElementErrorSourceSelfie(Type):
    # The selfie with the document contains an error. The error
    # will be considered resolved when the file with the selfie changes

    pass


class passportElementErrorSourceTranslationFile(Type):
    # One of files with the translation of the document contains
    # an error. The error will be considered resolved when the file changes

    pass


class passportElementErrorSourceTranslationFiles(Type):
    # The translation of the document contains an error. The error
    # will be considered resolved when the list of translation files changes

    pass


class passportElementErrorSourceFile(Type):
    # The file contains an error. The error will be considered
    # resolved when the file changes

    pass


class passportElementErrorSourceFiles(Type):
    # The list of attached files contains an error. The error
    # will be considered resolved when the list of files changes

    pass
