from tdwrapper.factory import Type


class gameHighScore(Type):
    #  one row of the game high score table @position
    #  in the high score table @user_id User identifier @score User score

    position = None  # type: "int32"
    user_id = None  # type: "int32"
    score = None  # type: "int32"
