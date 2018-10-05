from tdwrapper.factory import Method, Type


class file(Type):
    #  a file

    id = None  # type: "int32"
    size = None  # type: "int32"
    expected_size = None  # type: "int32"
    local = None  # type: "localFile"
    remote = None  # type: "remoteFile"


class getFile(Method):
    #  information about a file; this is an offline request
    #  Identifier of the file to get

    file_id = None  # type: "int32"


class getRemoteFile(Method):
    #  information about a file by its remote ID; this
    #  an offline request. Can be used to register a
    #  as a file for further uploading, or sending as
    #  message @remote_file_id Remote identifier of the file to get
    #  File type, if known

    remote_file_id = None  # type: "string"
    file_type = None  # type: "FileType"


class downloadFile(Method):
    #  downloads a file from the cloud. updateFile will be
    #  to notify about the download progress and successful completion
    #  the download. Returns file state just after the download has been started

    file_id = None  # type: "int32"
    priority = None  # type: "int32"


class uploadFile(Method):
    #  uploads a file to the cloud without sending it
    #  a message. updateFile will be used to notify about
    #  progress and successful completion of the upload. The file
    #  not have a persistent remote identifier until it will
    #  sent in a message @file File to upload @file_type File type

    file = None  # type: "InputFile"
    file_type = None  # type: "FileType"
    priority = None  # type: "int32"


class uploadStickerFile(Method):
    #  a PNG image with a sticker; for bots only;
    #  the uploaded file @user_id Sticker file owner @png_sticker PNG
    #  with the sticker; must be up to 512 kB
    #  size and fit in 512x512 square

    user_id = None  # type: "int32"
    png_sticker = None  # type: "InputFile"


class getMapThumbnailFile(Method):
    #  information about a file with a map thumbnail in
    #  format. Only map thumbnail files with size less than
    #  can be downloaded @location Location of the map center
    #  Map zoom level; 13-20 @width Map width in pixels
    #  applying scale; 16-1024 @height Map height in pixels before
    #  scale; 16-1024 @scale Map scale; 1-3 @chat_id Identifier of
    #  chat, in which the thumbnail will be shown. Use 0 if unknown

    location = None  # type: "location"
    zoom = None  # type: "int32"
    width = None  # type: "int32"
    height = None  # type: "int32"
    scale = None  # type: "int32"
    chat_id = None  # type: "int53"
