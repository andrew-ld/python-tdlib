from tdwrapper.factory import Method, Type


class languagePackStrings(Type):
    #  a list of language pack strings @strings A list
    #  language pack strings

    strings = None  # type: "vector<languagePackString>"


class getLanguagePackStrings(Method):
    #  strings from a language pack in the current localization
    #  by their keys @language_pack_id Language pack identifier of the
    #  to be returned @keys Language pack keys of the
    #  to be returned; leave empty to request all available

    language_pack_id = None  # type: "string"
    keys = None  # type: "vector<string>"
