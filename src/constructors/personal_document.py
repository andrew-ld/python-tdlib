from ..factory import Type


class personalDocument(Type):
    #  personal document, containing some information about a user @files
    #  of files containing the pages of the document @translation
    #  of files containing a certified English translation of the

    files = None  # type: "vector<datedFile>"
    translation = None  # type: "vector<datedFile>"
