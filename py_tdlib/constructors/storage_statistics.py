from ..factory import Method, Type


class storageStatistics(Type):
    #  the exact storage usage statistics split by chats and
    #  type @size Total size of files @count Total number
    #  files @by_chat Statistics split by chats

    size = None  # type: "int53"
    count = None  # type: "int32"
    by_chat = None  # type: "vector<storageStatisticsByChat>"


class getStorageStatistics(Method):
    #  storage usage statistics @chat_limit Maximum number of chats with
    #  largest storage usage for which separate statistics should be
    #  All other chats will be grouped in entries with
    #  == 0. If the chat info database is not
    #  the chat_limit is ignored and is always set to

    chat_limit = None  # type: "int32"


class optimizeStorage(Method):
    #  storage usage, i.e. deletes some files and returns new
    #  usage statistics. Secret thumbnails can't be deleted

    size = None  # type: "int53"
    ttl = None  # type: "int32"
    count = None  # type: "int32"
    immunity_delay = None  # type: "int32"
    file_types = None  # type: "vector<FileType>"
    chat_ids = None  # type: "vector<int53>"
    exclude_chat_ids = None  # type: "vector<int53>"
    chat_limit = None  # type: "int32"
