from ..factory import Type


class storageStatisticsByFileType(Type):
    # Contains the storage usage statistics for a specific file type
    # @file_type File type @size Total size of the files @count
    # Total number of files

    file_type = None  # type: "FileType"
    size = None  # type: "int53"
    count = None  # type: "int32"
