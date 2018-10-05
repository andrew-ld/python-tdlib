from tdwrapper.factory import Type


class localFile(Type):
    #  a local file

    path = None  # type: "string"
    can_be_downloaded = None  # type: "Bool"
    can_be_deleted = None  # type: "Bool"
    is_downloading_active = None  # type: "Bool"
    is_downloading_completed = None  # type: "Bool"
    downloaded_prefix_size = None  # type: "int32"
    downloaded_size = None  # type: "int32"
