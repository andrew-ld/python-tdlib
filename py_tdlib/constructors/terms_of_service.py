from ..factory import Type


class termsOfService(Type):
    #  Telegram terms of service @text Text of the terms
    #  service @min_user_age Mininum age of a user to be
    #  to accept the terms; 0 if any @show_popup True,
    #  a blocking popup with terms of service must be
    #  to the user

    text = None  # type: "formattedText"
    min_user_age = None  # type: "int32"
    show_popup = None  # type: "Bool"
