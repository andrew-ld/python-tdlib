from ..factory import Method, Type


class languagePackStrings(Type):
    # Contains a list of language pack strings, @strings A list
    # of language pack strings

    strings = None  # type: "vector<languagePackString>"


class getLanguagePackStrings(Method):
    # Returns strings from a language pack in the current localization
    # target by their keys, @language_pack_id Language pack identifier of the
    # strings to be returned, @keys Language pack keys of the
    # strings to be returned; leave empty to request all available strings

    language_pack_id = None  # type: "string"
    keys = None  # type: "vector<string>"
