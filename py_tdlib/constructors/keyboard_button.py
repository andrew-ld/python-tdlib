from ..factory import Type


class keyboardButton(Type):
    # Represents a single button in a bot keyboard, @text Text
    # of the button, @type Type of the button

    text = None  # type: "string"
    type = None  # type: "KeyboardButtonType"
