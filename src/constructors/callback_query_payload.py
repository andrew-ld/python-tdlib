from tdwrapper.factory import Type


class callbackQueryPayloadData(Type):
    #  payload from a general callback button @data Data that
    #  attached to the callback button

    data = None  # type: "bytes"


class callbackQueryPayloadGame(Type):
    #  payload from a game callback button @game_short_name A short
    #  of the game that was attached to the callback

    game_short_name = None  # type: "string"
