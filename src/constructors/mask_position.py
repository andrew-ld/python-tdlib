from tdwrapper.factory import Type


class maskPosition(Type):
    #  on a photo where a mask should be placed
    #  Part of the face, relative to which the mask should be placed

    point = None  # type: "MaskPoint"
    x_shift = None  # type: "double"
    y_shift = None  # type: "double"
    scale = None  # type: "double"
