from ..factory import Type


class inputPersonalDocument(Type):
    # A personal document to be saved to Telegram Passport, @files
    # List of files containing the pages of the document, @translation
    # List of files containing a certified English translation of the document

    files = None  # type: "vector<InputFile>"
    translation = None  # type: "vector<InputFile>"
