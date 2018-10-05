from tdwrapper.factory import Type


class keyboardButtonTypeText(Type):
    #  simple button, with text that should be sent when
    #  button is pressed

    pass


class keyboardButtonTypeRequestPhoneNumber(Type):
    #  button that sends the user's phone number when pressed;
    #  only in private chats

    pass


class keyboardButtonTypeRequestLocation(Type):
    #  button that sends the user's location when pressed; available
    #  in private chats

    pass
