from ..factory import Type


class wallpaper(Type):
    # Contains information about a wallpaper, @id Unique persistent wallpaper identifier
    # @sizes Available variants of the wallpaper in different sizes. These
    # photos can only be downloaded; they can't be sent in
    # a message, @color Main color of the wallpaper in RGB24
    # format; should be treated as background color if no photos are specified

    id = None  # type: "int32"
    sizes = None  # type: "vector<photoSize>"
    color = None  # type: "int32"
