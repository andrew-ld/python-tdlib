from ..factory import Type


class callbackQueryPayloadData(Type):
    # The payload from a general callback button, @data Data that
    # was attached to the callback button

    data = None  # type: "bytes"


class callbackQueryPayloadGame(Type):
    # The payload from a game callback button, @game_short_name A short
    # name of the game that was attached to the callback button

    game_short_name = None  # type: "string"
