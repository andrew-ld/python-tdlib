from ..factory import Type


class connectedWebsite(Type):
    #  information about one website the current user is logged in with Telegram

    id = None  # type: "int64"
    domain_name = None  # type: "string"
    bot_user_id = None  # type: "int32"
    browser = None  # type: "string"
    platform = None  # type: "string"
    log_in_date = None  # type: "int32"
    last_active_date = None  # type: "int32"
    ip = None  # type: "string"
    location = None  # type: "string"
