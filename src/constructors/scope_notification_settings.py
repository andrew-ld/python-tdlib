from tdwrapper.factory import Method, Type


class scopeNotificationSettings(Type):
    #  information about notification settings for several chats @mute_for Time
    #  before notifications will be unmuted, in seconds

    mute_for = None  # type: "int32"
    sound = None  # type: "string"
    show_preview = None  # type: "Bool"


class getScopeNotificationSettings(Method):
    #  the notification settings for chats of a given type
    #  Types of chats for which to return the notification settings information

    scope = None  # type: "NotificationSettingsScope"
