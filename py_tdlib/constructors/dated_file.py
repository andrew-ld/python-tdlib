from ..factory import Type


class datedFile(Type):
    # File with the date it was uploaded, @file The file
    # @date Point in time (Unix timestamp) when the file was uploaded

    file = None  # type: "file"
    date = None  # type: "int32"
