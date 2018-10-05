from tdwrapper.factory import Type


class languagePackInfo(Type):
    #  information about a language pack @id Unique language pack
    #  @name Language name @native_name Name of the language in
    #  language @local_string_count Total number of non-deleted strings from the
    #  pack available locally

    id = None  # type: "string"
    name = None  # type: "string"
    native_name = None  # type: "string"
    local_string_count = None  # type: "int32"
