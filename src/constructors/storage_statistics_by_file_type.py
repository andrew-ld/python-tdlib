from tdwrapper.factory import Type


class storageStatisticsByFileType(Type):
    #  the storage usage statistics for a specific file type
    #  File type @size Total size of the files @count
    #  number of files

    file_type = None  # type: "FileType"
    size = None  # type: "int53"
    count = None  # type: "int32"
