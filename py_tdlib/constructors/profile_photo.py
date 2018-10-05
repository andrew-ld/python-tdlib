from ..factory import Type


class profilePhoto(Type):
    # Describes a user profile photo @id Photo identifier; 0 for
    # an empty photo. Can be used to find a photo
    # in a list of userProfilePhotos

    id = None  # type: "int64"
    small = None  # type: "file"
    big = None  # type: "file"
