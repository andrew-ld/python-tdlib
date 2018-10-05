from ..factory import Type


class passportElementErrorSourceUnspecified(Type):
    #  element contains an error in an unspecified place. The
    #  will be considered resolved when new data is added

    pass


class passportElementErrorSourceDataField(Type):
    #  of the data fields contains an error. The error
    #  be considered resolved when the value of the field
    #  @field_name Field name

    field_name = None  # type: "string"


class passportElementErrorSourceFrontSide(Type):
    #  front side of the document contains an error. The
    #  will be considered resolved when the file with the front side changes

    pass


class passportElementErrorSourceReverseSide(Type):
    #  reverse side of the document contains an error. The
    #  will be considered resolved when the file with the reverse side changes

    pass


class passportElementErrorSourceSelfie(Type):
    #  selfie with the document contains an error. The error
    #  be considered resolved when the file with the selfie

    pass


class passportElementErrorSourceTranslationFile(Type):
    #  of files with the translation of the document contains
    #  error. The error will be considered resolved when the file changes

    pass


class passportElementErrorSourceTranslationFiles(Type):
    #  translation of the document contains an error. The error
    #  be considered resolved when the list of translation files

    pass


class passportElementErrorSourceFile(Type):
    #  file contains an error. The error will be considered
    #  when the file changes

    pass


class passportElementErrorSourceFiles(Type):
    #  list of attached files contains an error. The error
    #  be considered resolved when the list of files changes

    pass
