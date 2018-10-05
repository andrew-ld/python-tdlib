from ..factory import Type


class inputPersonalDocument(Type):
    #  personal document to be saved to Telegram Passport @files
    #  of files containing the pages of the document @translation
    #  of files containing a certified English translation of the

    files = None  # type: "vector<InputFile>"
    translation = None  # type: "vector<InputFile>"
