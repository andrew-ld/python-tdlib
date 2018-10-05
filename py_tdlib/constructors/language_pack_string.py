from ..factory import Type


class languagePackString(Type):
    # Represents one language pack string @key String key @value String value

    key = None  # type: "string"
    value = None  # type: "LanguagePackStringValue"
