from tdwrapper.factory import Method, Type


class languagePackStringValueOrdinary(Type):
    #  ordinary language pack string @value String value

    value = None  # type: "string"


class languagePackStringValuePluralized(Type):
    #  language pack string which has different forms based on
    #  number of some object it mentions @zero_value Value for
    #  objects @one_value Value for one object @two_value Value for two objects

    zero_value = None  # type: "string"
    one_value = None  # type: "string"
    two_value = None  # type: "string"
    few_value = None  # type: "string"
    many_value = None  # type: "string"
    other_value = None  # type: "string"


class languagePackStringValueDeleted(Type):
    #  deleted language pack string, the value should be taken
    #  the built-in english language pack

    pass


class getLanguagePackString(Method):
    #  a string stored in the local database from the
    #  localization target and language pack by its key. Returns
    #  404 error if the string is not found. This
    #  an offline method. Can be called before authorization. Can be called synchronously

    language_pack_database_path = None  # type: "string"
    localization_target = None  # type: "string"
    language_pack_id = None  # type: "string"
    key = None  # type: "string"
