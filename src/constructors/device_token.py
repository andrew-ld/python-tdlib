from tdwrapper.factory import Type


class deviceTokenGoogleCloudMessaging(Type):
    #  token for Google Cloud Messaging @token Device registration token;
    #  be empty to de-register a device

    token = None  # type: "string"


class deviceTokenApplePush(Type):
    #  token for Apple Push Notification service @device_token Device token;
    #  be empty to de-register a device @is_app_sandbox True, if
    #  Sandbox is enabled

    device_token = None  # type: "string"
    is_app_sandbox = None  # type: "Bool"


class deviceTokenApplePushVoIP(Type):
    #  token for Apple Push Notification service VoIP notifications @device_token
    #  token; may be empty to de-register a device @is_app_sandbox
    #  if App Sandbox is enabled

    device_token = None  # type: "string"
    is_app_sandbox = None  # type: "Bool"


class deviceTokenWindowsPush(Type):
    #  token for Windows Push Notification Services @access_token The access
    #  that will be used to send notifications; may be
    #  to de-register a device

    access_token = None  # type: "string"


class deviceTokenMicrosoftPush(Type):
    #  token for Microsoft Push Notification Service @channel_uri Push notification
    #  URI; may be empty to de-register a device

    channel_uri = None  # type: "string"


class deviceTokenMicrosoftPushVoIP(Type):
    #  token for Microsoft Push Notification Service VoIP channel @channel_uri
    #  notification channel URI; may be empty to de-register a

    channel_uri = None  # type: "string"


class deviceTokenWebPush(Type):
    #  token for web Push API @endpoint Absolute URL exposed
    #  the push service where the application server can send
    #  messages; may be empty to de-register a device

    endpoint = None  # type: "string"
    p256dh_base64url = None  # type: "string"
    auth_base64url = None  # type: "string"


class deviceTokenSimplePush(Type):
    #  token for Simple Push API for Firefox OS @endpoint
    #  URL exposed by the push service where the application
    #  can send push messages; may be empty to de-register a device

    endpoint = None  # type: "string"


class deviceTokenUbuntuPush(Type):
    #  token for Ubuntu Push Client service @token Token; may
    #  empty to de-register a device

    token = None  # type: "string"


class deviceTokenBlackBerryPush(Type):
    #  token for BlackBerry Push Service @token Token; may be
    #  to de-register a device

    token = None  # type: "string"


class deviceTokenTizenPush(Type):
    #  token for Tizen Push Service @reg_id Push service registration
    #  may be empty to de-register a device

    reg_id = None  # type: "string"
