from tdwrapper.factory import Type


class chatNotificationSettings(Type):
    #  information about notification settings for a chat

    use_default_mute_for = None  # type: "Bool"
    mute_for = None  # type: "int32"
    use_default_sound = None  # type: "Bool"
    sound = None  # type: "string"
    use_default_show_preview = None  # type: "Bool"
    show_preview = None  # type: "Bool"
