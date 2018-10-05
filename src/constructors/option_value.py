from tdwrapper.factory import Method, Type


class optionValueBoolean(Type):
    #  option @value The value of the option

    value = None  # type: "Bool"


class optionValueEmpty(Type):
    #  unknown option or an option which has a default

    pass


class optionValueInteger(Type):
    #  integer option @value The value of the option

    value = None  # type: "int32"


class optionValueString(Type):
    #  string option @value The value of the option

    value = None  # type: "string"


class getOption(Method):
    #  the value of an option by its name. (Check
    #  list of available options on https://core.telegram.org/tdlib/options.) Can be called before authorization

    name = None  # type: "string"
