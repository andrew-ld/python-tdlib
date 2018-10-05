from ..factory import Type


class profilePhoto(Type):
    #  a user profile photo @id Photo identifier; 0 for
    #  empty photo. Can be used to find a photo
    #  a list of userProfilePhotos

    id = None  # type: "int64"
    small = None  # type: "file"
    big = None  # type: "file"
