from tdwrapper.factory import Method, Type


class storageStatisticsFast(Type):
    #  approximate storage usage statistics, excluding files of unknown file
    #  @files_size Approximate total size of files @file_count Approximate number
    #  files @database_size Size of the database

    files_size = None  # type: "int53"
    file_count = None  # type: "int32"
    database_size = None  # type: "int53"


class getStorageStatisticsFast(Method):
    #  returns approximate storage usage statistics

    pass
