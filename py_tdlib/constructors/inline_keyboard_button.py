from ..factory import Type


class inlineKeyboardButton(Type):
    # Represents a single button in an inline keyboard @text Text
    # of the button @type Type of the button

    text = None  # type: "string"
    type = None  # type: "InlineKeyboardButtonType"
