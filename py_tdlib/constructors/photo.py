from ..factory import Type


class photo(Type):
    # Describes a photo @id Photo identifier; 0 for deleted photos
    # @has_stickers True, if stickers were added to the photo @sizes
    # Available variants of the photo, in different sizes

    id = None  # type: "int64"
    has_stickers = None  # type: "Bool"
    sizes = None  # type: "vector<photoSize>"
