from tdwrapper.factory import Type


class wallpaper(Type):
    #  information about a wallpaper @id Unique persistent wallpaper identifier
    #  Available variants of the wallpaper in different sizes. These
    #  can only be downloaded; they can't be sent in
    #  message @color Main color of the wallpaper in RGB24
    #  should be treated as background color if no photos are specified

    id = None  # type: "int32"
    sizes = None  # type: "vector<photoSize>"
    color = None  # type: "int32"
