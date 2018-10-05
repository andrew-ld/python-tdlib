from ..factory import Type


class deviceTokenGoogleCloudMessaging(Type):
    # A token for Google Cloud Messaging @token Device registration token;
    # may be empty to de-register a device

    token = None  # type: "string"


class deviceTokenApplePush(Type):
    # A token for Apple Push Notification service @device_token Device token;
    # may be empty to de-register a device @is_app_sandbox True, if
    # App Sandbox is enabled

    device_token = None  # type: "string"
    is_app_sandbox = None  # type: "Bool"


class deviceTokenApplePushVoIP(Type):
    # A token for Apple Push Notification service VoIP notifications @device_token
    # Device token; may be empty to de-register a device @is_app_sandbox
    # True, if App Sandbox is enabled

    device_token = None  # type: "string"
    is_app_sandbox = None  # type: "Bool"


class deviceTokenWindowsPush(Type):
    # A token for Windows Push Notification Services @access_token The access
    # token that will be used to send notifications; may be
    # empty to de-register a device

    access_token = None  # type: "string"


class deviceTokenMicrosoftPush(Type):
    # A token for Microsoft Push Notification Service @channel_uri Push notification
    # channel URI; may be empty to de-register a device

    channel_uri = None  # type: "string"


class deviceTokenMicrosoftPushVoIP(Type):
    # A token for Microsoft Push Notification Service VoIP channel @channel_uri
    # Push notification channel URI; may be empty to de-register a device

    channel_uri = None  # type: "string"


class deviceTokenWebPush(Type):
    # A token for web Push API @endpoint Absolute URL exposed
    # by the push service where the application server can send
    # push messages; may be empty to de-register a device

    endpoint = None  # type: "string"
    p256dh_base64url = None  # type: "string"
    auth_base64url = None  # type: "string"


class deviceTokenSimplePush(Type):
    # A token for Simple Push API for Firefox OS @endpoint
    # Absolute URL exposed by the push service where the application
    # server can send push messages; may be empty to de-register a device

    endpoint = None  # type: "string"


class deviceTokenUbuntuPush(Type):
    # A token for Ubuntu Push Client service @token Token; may
    # be empty to de-register a device

    token = None  # type: "string"


class deviceTokenBlackBerryPush(Type):
    # A token for BlackBerry Push Service @token Token; may be
    # empty to de-register a device

    token = None  # type: "string"


class deviceTokenTizenPush(Type):
    # A token for Tizen Push Service @reg_id Push service registration
    # identifier; may be empty to de-register a device

    reg_id = None  # type: "string"
