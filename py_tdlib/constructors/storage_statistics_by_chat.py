from ..factory import Type


class storageStatisticsByChat(Type):
    # Contains the storage usage statistics for a specific chat, @chat_id
    # Chat identifier; 0 if none, @size Total size of the
    # files in the chat, @count Total number of files in
    # the chat, @by_file_type Statistics split by file types

    chat_id = None  # type: "int53"
    size = None  # type: "int53"
    count = None  # type: "int32"
    by_file_type = None  # type: "vector<storageStatisticsByFileType>"
