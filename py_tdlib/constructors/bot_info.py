from ..factory import Type


class botInfo(Type):
    #  information about a bot and its supported commands @param_description
    #  description shown on the user info page @commands A
    #  of commands supported by the bot

    description = None  # type: "string"
    commands = None  # type: "vector<botCommand>"
