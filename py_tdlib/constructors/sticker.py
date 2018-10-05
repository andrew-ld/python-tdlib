from ..factory import Type


class sticker(Type):
    # Describes a sticker @set_id The identifier of the sticker set
    # to which the sticker belongs; 0 if none @width Sticker
    # width; as defined by the sender @height Sticker height; as
    # defined by the sender

    set_id = None  # type: "int64"
    width = None  # type: "int32"
    height = None  # type: "int32"
    emoji = None  # type: "string"
    is_mask = None  # type: "Bool"
    mask_position = None  # type: "maskPosition"
    thumbnail = None  # type: "photoSize"
    sticker = None  # type: "file"
