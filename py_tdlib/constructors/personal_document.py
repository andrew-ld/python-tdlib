from ..factory import Type


class personalDocument(Type):
    # A personal document, containing some information about a user @files
    # List of files containing the pages of the document @translation
    # List of files containing a certified English translation of the document

    files = None  # type: "vector<datedFile>"
    translation = None  # type: "vector<datedFile>"
