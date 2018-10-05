from ..factory import Type


class languagePackInfo(Type):
    # Contains information about a language pack @id Unique language pack
    # identifier @name Language name @native_name Name of the language in
    # that language @local_string_count Total number of non-deleted strings from the
    # language pack available locally

    id = None  # type: "string"
    name = None  # type: "string"
    native_name = None  # type: "string"
    local_string_count = None  # type: "int32"
