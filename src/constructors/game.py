from tdwrapper.factory import Type


class game(Type):
    #  a game @id Game ID @short_name Game short name.
    #  share a game use the URL https://t.me/{bot_username}?game={game_short_name} @title Game
    #  @text Game text, usually containing scoreboards for a game

    id = None  # type: "int64"
    short_name = None  # type: "string"
    title = None  # type: "string"
    text = None  # type: "formattedText"
    description = None  # type: "string"
    photo = None  # type: "photo"
    animation = None  # type: "animation"
