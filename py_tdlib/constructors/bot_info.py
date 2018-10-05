from ..factory import Type


class botInfo(Type):
    # Provides information about a bot and its supported commands, @param_description
    # Long description shown on the user info page, @commands A
    # list of commands supported by the bot

    description = None  # type: "string"
    commands = None  # type: "vector<botCommand>"
