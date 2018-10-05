from ..factory import Method, Type


class optionValueBoolean(Type):
    # Boolean option, @value The value of the option

    value = None  # type: "Bool"


class optionValueEmpty(Type):
    # An unknown option or an option which has a default value

    pass


class optionValueInteger(Type):
    # An integer option, @value The value of the option

    value = None  # type: "int32"


class optionValueString(Type):
    # A string option, @value The value of the option

    value = None  # type: "string"


class getOption(Method):
    # Returns the value of an option by its name. (Check
    # the list of available options on https://core.telegram.org/tdlib/options.) Can be called before authorization

    name = None  # type: "string"
