from ..factory import Type


class textEntity(Type):
    # Represents a part of the text that needs to be
    # formatted in some unusual way @offset Offset of the entity
    # in UTF-16 code points @length Length of the entity, in
    # UTF-16 code points @type Type of the entity

    offset = None  # type: "int32"
    length = None  # type: "int32"
    type = None  # type: "TextEntityType"
