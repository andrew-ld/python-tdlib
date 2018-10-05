from tdwrapper.factory import Type


class photo(Type):
    #  a photo @id Photo identifier; 0 for deleted photos
    #  True, if stickers were added to the photo @sizes
    #  variants of the photo, in different sizes

    id = None  # type: "int64"
    has_stickers = None  # type: "Bool"
    sizes = None  # type: "vector<photoSize>"
