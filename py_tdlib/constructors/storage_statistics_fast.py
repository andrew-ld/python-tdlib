from ..factory import Method, Type


class storageStatisticsFast(Type):
    # Contains approximate storage usage statistics, excluding files of unknown file
    # type, @files_size Approximate total size of files, @file_count Approximate number
    # of files, @database_size Size of the database

    files_size = None  # type: "int53"
    file_count = None  # type: "int32"
    database_size = None  # type: "int53"


class getStorageStatisticsFast(Method):
    # Quickly returns approximate storage usage statistics

    pass
