from ..factory import Type


class keyboardButtonTypeText(Type):
    # A simple button, with text that should be sent when
    # the button is pressed

    pass


class keyboardButtonTypeRequestPhoneNumber(Type):
    # A button that sends the user's phone number when pressed;
    # available only in private chats

    pass


class keyboardButtonTypeRequestLocation(Type):
    # A button that sends the user's location when pressed; available
    # only in private chats

    pass
