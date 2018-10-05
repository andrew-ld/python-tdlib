from ..factory import Method, Type


class storageStatistics(Type):
    # Contains the exact storage usage statistics split by chats and
    # file type @size Total size of files @count Total number
    # of files @by_chat Statistics split by chats

    size = None  # type: "int53"
    count = None  # type: "int32"
    by_chat = None  # type: "vector<storageStatisticsByChat>"


class getStorageStatistics(Method):
    # Returns storage usage statistics @chat_limit Maximum number of chats with
    # the largest storage usage for which separate statistics should be
    # returned. All other chats will be grouped in entries with
    # chat_id == 0. If the chat info database is not
    # used, the chat_limit is ignored and is always set to 0

    chat_limit = None  # type: "int32"


class optimizeStorage(Method):
    # Optimizes storage usage, i.e. deletes some files and returns new
    # storage usage statistics. Secret thumbnails can't be deleted

    size = None  # type: "int53"
    ttl = None  # type: "int32"
    count = None  # type: "int32"
    immunity_delay = None  # type: "int32"
    file_types = None  # type: "vector<FileType>"
    chat_ids = None  # type: "vector<int53>"
    exclude_chat_ids = None  # type: "vector<int53>"
    chat_limit = None  # type: "int32"
