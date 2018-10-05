from tdwrapper.factory import Type


class inlineKeyboardButton(Type):
    #  a single button in an inline keyboard @text Text
    #  the button @type Type of the button

    text = None  # type: "string"
    type = None  # type: "InlineKeyboardButtonType"
