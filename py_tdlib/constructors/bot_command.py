from ..factory import Type


class botCommand(Type):
    # Represents commands supported by a bot @command Text of the
    # bot command @param_description Description of the bot command

    command = None  # type: "string"
    description = None  # type: "string"
