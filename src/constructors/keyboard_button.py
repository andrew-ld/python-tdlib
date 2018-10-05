from tdwrapper.factory import Type


class keyboardButton(Type):
    #  a single button in a bot keyboard @text Text
    #  the button @type Type of the button

    text = None  # type: "string"
    type = None  # type: "KeyboardButtonType"
