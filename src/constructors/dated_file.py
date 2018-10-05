from ..factory import Type


class datedFile(Type):
    #  with the date it was uploaded @file The file
    #  Point in time (Unix timestamp) when the file was

    file = None  # type: "file"
    date = None  # type: "int32"
