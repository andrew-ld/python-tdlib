from tdwrapper.factory import Type


class remoteFile(Type):
    #  a remote file

    id = None  # type: "string"
    is_uploading_active = None  # type: "Bool"
    is_uploading_completed = None  # type: "Bool"
    uploaded_size = None  # type: "int32"
