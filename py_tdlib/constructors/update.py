from ..factory import Method, Type


class updateAuthorizationState(Type):
    # The user authorization state has changed @authorization_state New authorization state

    authorization_state = None  # type: "AuthorizationState"


class updateNewMessage(Type):
    # A new message was received; can also be an outgoing
    # message @message The new message @disable_notification True, if this message
    # must not generate a notification @contains_mention True, if the message
    # contains a mention of the current user

    message = None  # type: "message"
    disable_notification = None  # type: "Bool"
    contains_mention = None  # type: "Bool"


class updateMessageSendAcknowledged(Type):
    # A request to send a message has reached the Telegram
    # server. This doesn't mean that the message will be sent
    # successfully or even that the send message request will be
    # processed. This update will be sent only if the option
    # "use_quick_ack" is set to true. This update may be sent
    # multiple times for the same message

    chat_id = None  # type: "int53"
    message_id = None  # type: "int53"


class updateMessageSendSucceeded(Type):
    # A message has been successfully sent @message Information about the
    # sent message. Usually only the message identifier, date, and content
    # are changed, but almost all other fields can also change
    # @old_message_id The previous temporary message identifier

    message = None  # type: "message"
    old_message_id = None  # type: "int53"


class updateMessageSendFailed(Type):
    # A message failed to send. Be aware that some messages
    # being sent can be irrecoverably deleted, in which case updateDeleteMessages
    # will be received instead of this update

    message = None  # type: "message"
    old_message_id = None  # type: "int53"
    error_code = None  # type: "int32"
    error_message = None  # type: "string"


class updateMessageContent(Type):
    # The message content has changed @chat_id Chat identifier @message_id Message
    # identifier @new_content New message content

    chat_id = None  # type: "int53"
    message_id = None  # type: "int53"
    new_content = None  # type: "MessageContent"


class updateMessageEdited(Type):
    # A message was edited. Changes in the message content will
    # come in a separate updateMessageContent @chat_id Chat identifier @message_id Message
    # identifier @edit_date Point in time (Unix timestamp) when the message
    # was edited @reply_markup New message reply markup; may be null

    chat_id = None  # type: "int53"
    message_id = None  # type: "int53"
    edit_date = None  # type: "int32"
    reply_markup = None  # type: "ReplyMarkup"


class updateMessageViews(Type):
    # The view count of the message has changed @chat_id Chat
    # identifier @message_id Message identifier @views New value of the view count

    chat_id = None  # type: "int53"
    message_id = None  # type: "int53"
    views = None  # type: "int32"


class updateMessageContentOpened(Type):
    # The message content was opened. Updates voice note messages to
    # "listened", video note messages to "viewed" and starts the TTL
    # timer for self-destructing messages @chat_id Chat identifier @message_id Message identifier

    chat_id = None  # type: "int53"
    message_id = None  # type: "int53"


class updateMessageMentionRead(Type):
    # A message with an unread mention was read @chat_id Chat
    # identifier @message_id Message identifier @unread_mention_count The new number of unread
    # mention messages left in the chat

    chat_id = None  # type: "int53"
    message_id = None  # type: "int53"
    unread_mention_count = None  # type: "int32"


class updateNewChat(Type):
    # A new chat has been loaded/created. This update is guaranteed
    # to come before the chat identifier is returned to the
    # client. The chat field changes will be reported through separate
    # updates @chat The chat

    chat = None  # type: "chat"


class updateChatTitle(Type):
    # The title of a chat was changed @chat_id Chat identifier
    # @title The new chat title

    chat_id = None  # type: "int53"
    title = None  # type: "string"


class updateChatPhoto(Type):
    # A chat photo was changed @chat_id Chat identifier @photo The
    # new chat photo; may be null

    chat_id = None  # type: "int53"
    photo = None  # type: "chatPhoto"


class updateChatLastMessage(Type):
    # The last message of a chat was changed. If last_message
    # is null then the last message in the chat became
    # unknown. Some new unknown messages might be added to the
    # chat in this case @chat_id Chat identifier @last_message The new
    # last message in the chat; may be null @order New
    # value of the chat order

    chat_id = None  # type: "int53"
    last_message = None  # type: "message"
    order = None  # type: "int64"


class updateChatOrder(Type):
    # The order of the chat in the chats list has
    # changed. Instead of this update updateChatLastMessage, updateChatIsPinned or updateChatDraftMessage might
    # be sent @chat_id Chat identifier @order New value of the order

    chat_id = None  # type: "int53"
    order = None  # type: "int64"


class updateChatIsPinned(Type):
    # A chat was pinned or unpinned @chat_id Chat identifier @is_pinned
    # New value of is_pinned @order New value of the chat order

    chat_id = None  # type: "int53"
    is_pinned = None  # type: "Bool"
    order = None  # type: "int64"


class updateChatIsMarkedAsUnread(Type):
    # A chat was marked as unread or was read @chat_id
    # Chat identifier @is_marked_as_unread New value of is_marked_as_unread

    chat_id = None  # type: "int53"
    is_marked_as_unread = None  # type: "Bool"


class updateChatIsSponsored(Type):
    # A chat's is_sponsored field has changed @chat_id Chat identifier @is_sponsored
    # New value of is_sponsored @order New value of chat order

    chat_id = None  # type: "int53"
    is_sponsored = None  # type: "Bool"
    order = None  # type: "int64"


class updateChatDefaultDisableNotification(Type):
    # The value of the default disable_notification parameter, used when a
    # message is sent to the chat, was changed @chat_id Chat
    # identifier @default_disable_notification The new default_disable_notification value

    chat_id = None  # type: "int53"
    default_disable_notification = None  # type: "Bool"


class updateChatReadInbox(Type):
    # Incoming messages were read or number of unread messages has
    # been changed @chat_id Chat identifier @last_read_inbox_message_id Identifier of the last
    # read incoming message @unread_count The number of unread messages left in the chat

    chat_id = None  # type: "int53"
    last_read_inbox_message_id = None  # type: "int53"
    unread_count = None  # type: "int32"


class updateChatReadOutbox(Type):
    # Outgoing messages were read @chat_id Chat identifier @last_read_outbox_message_id Identifier of
    # last read outgoing message

    chat_id = None  # type: "int53"
    last_read_outbox_message_id = None  # type: "int53"


class updateChatUnreadMentionCount(Type):
    # The chat unread_mention_count has changed @chat_id Chat identifier @unread_mention_count The
    # number of unread mention messages left in the chat

    chat_id = None  # type: "int53"
    unread_mention_count = None  # type: "int32"


class updateChatNotificationSettings(Type):
    # Notification settings for a chat were changed @chat_id Chat identifier
    # @notification_settings The new notification settings

    chat_id = None  # type: "int53"
    notification_settings = None  # type: "chatNotificationSettings"


class updateScopeNotificationSettings(Type):
    # Notification settings for some type of chats were updated @scope
    # Types of chats for which notification settings were updated @notification_settings
    # The new notification settings

    scope = None  # type: "NotificationSettingsScope"
    notification_settings = None  # type: "scopeNotificationSettings"


class updateChatReplyMarkup(Type):
    # The default chat reply markup was changed. Can occur because
    # new messages with reply markup were received or because an
    # old reply markup was hidden by the user

    chat_id = None  # type: "int53"
    reply_markup_message_id = None  # type: "int53"


class updateChatDraftMessage(Type):
    # A chat draft has changed. Be aware that the update
    # may come in the currently opened chat but with old
    # content of the draft. If the user has changed the
    # content of the draft, this update shouldn't be applied @chat_id
    # Chat identifier @draft_message The new draft message; may be null
    # @order New value of the chat order

    chat_id = None  # type: "int53"
    draft_message = None  # type: "draftMessage"
    order = None  # type: "int64"


class updateDeleteMessages(Type):
    # Some messages were deleted @chat_id Chat identifier @message_ids Identifiers of the deleted messages

    chat_id = None  # type: "int53"
    message_ids = None  # type: "vector<int53>"
    is_permanent = None  # type: "Bool"
    from_cache = None  # type: "Bool"


class updateUserChatAction(Type):
    # User activity in the chat has changed @chat_id Chat identifier
    # @user_id Identifier of a user performing an action @action The action description

    chat_id = None  # type: "int53"
    user_id = None  # type: "int32"
    action = None  # type: "ChatAction"


class updateUserStatus(Type):
    # The user went online or offline @user_id User identifier @status
    # New status of the user

    user_id = None  # type: "int32"
    status = None  # type: "UserStatus"


class updateUser(Type):
    # Some data of a user has changed. This update is
    # guaranteed to come before the user identifier is returned to
    # the client @user New data about the user

    user = None  # type: "user"


class updateBasicGroup(Type):
    # Some data of a basic group has changed. This update
    # is guaranteed to come before the basic group identifier is
    # returned to the client @basic_group New data about the group

    basic_group = None  # type: "basicGroup"


class updateSupergroup(Type):
    # Some data of a supergroup or a channel has changed.
    # This update is guaranteed to come before the supergroup identifier
    # is returned to the client @supergroup New data about the supergroup

    supergroup = None  # type: "supergroup"


class updateSecretChat(Type):
    # Some data of a secret chat has changed. This update
    # is guaranteed to come before the secret chat identifier is
    # returned to the client @secret_chat New data about the secret chat

    secret_chat = None  # type: "secretChat"


class updateUserFullInfo(Type):
    # Some data from userFullInfo has been changed @user_id User identifier
    # @user_full_info New full information about the user

    user_id = None  # type: "int32"
    user_full_info = None  # type: "userFullInfo"


class updateBasicGroupFullInfo(Type):
    # Some data from basicGroupFullInfo has been changed @basic_group_id Identifier of
    # a basic group @basic_group_full_info New full information about the group

    basic_group_id = None  # type: "int32"
    basic_group_full_info = None  # type: "basicGroupFullInfo"


class updateSupergroupFullInfo(Type):
    # Some data from supergroupFullInfo has been changed @supergroup_id Identifier of
    # the supergroup or channel @supergroup_full_info New full information about the supergroup

    supergroup_id = None  # type: "int32"
    supergroup_full_info = None  # type: "supergroupFullInfo"


class updateServiceNotification(Type):
    # Service notification from the server. Upon receiving this the client
    # must show a popup with the content of the notification

    type = None  # type: "string"
    content = None  # type: "MessageContent"


class updateFile(Type):
    # Information about a file was updated @file New data about the file

    file = None  # type: "file"


class updateFileGenerationStart(Type):
    # The file generation process needs to be started by the client

    generation_id = None  # type: "int64"
    original_path = None  # type: "string"
    destination_path = None  # type: "string"
    conversion = None  # type: "string"


class updateFileGenerationStop(Type):
    # File generation is no longer needed @generation_id Unique identifier for the generation process

    generation_id = None  # type: "int64"


class updateCall(Type):
    # New call was created or information about a call was
    # updated @call New data about a call

    call = None  # type: "call"


class updateUserPrivacySettingRules(Type):
    # Some privacy setting rules have been changed @setting The privacy
    # setting @rules New privacy rules

    setting = None  # type: "UserPrivacySetting"
    rules = None  # type: "userPrivacySettingRules"


class updateUnreadMessageCount(Type):
    # Number of unread messages has changed. This update is sent
    # only if a message database is used @unread_count Total number
    # of unread messages @unread_unmuted_count Total number of unread messages in unmuted chats

    unread_count = None  # type: "int32"
    unread_unmuted_count = None  # type: "int32"


class updateUnreadChatCount(Type):
    # Number of unread chats, i.e. with unread messages or marked
    # as unread, has changed. This update is sent only if
    # a message database is used

    unread_count = None  # type: "int32"
    unread_unmuted_count = None  # type: "int32"
    marked_as_unread_count = None  # type: "int32"
    marked_as_unread_unmuted_count = None  # type: "int32"


class updateOption(Type):
    # An option changed its value @name The option name @value
    # The new option value

    name = None  # type: "string"
    value = None  # type: "OptionValue"


class updateInstalledStickerSets(Type):
    # The list of installed sticker sets was updated @is_masks True,
    # if the list of installed mask sticker sets was updated
    # @sticker_set_ids The new list of installed ordinary sticker sets

    is_masks = None  # type: "Bool"
    sticker_set_ids = None  # type: "vector<int64>"


class updateTrendingStickerSets(Type):
    # The list of trending sticker sets was updated or some
    # of them were viewed @sticker_sets The new list of trending sticker sets

    sticker_sets = None  # type: "stickerSets"


class updateRecentStickers(Type):
    # The list of recently used stickers was updated @is_attached True,
    # if the list of stickers attached to photo or video
    # files was updated, otherwise the list of sent stickers is
    # updated @sticker_ids The new list of file identifiers of recently used stickers

    is_attached = None  # type: "Bool"
    sticker_ids = None  # type: "vector<int32>"


class updateFavoriteStickers(Type):
    # The list of favorite stickers was updated @sticker_ids The new
    # list of file identifiers of favorite stickers

    sticker_ids = None  # type: "vector<int32>"


class updateSavedAnimations(Type):
    # The list of saved animations was updated @animation_ids The new
    # list of file identifiers of saved animations

    animation_ids = None  # type: "vector<int32>"


class updateLanguagePackStrings(Type):
    # Some language pack strings have been updated @localization_target Localization target
    # to which the language pack belongs @language_pack_id Identifier of the
    # updated language pack @strings List of changed language pack strings

    localization_target = None  # type: "string"
    language_pack_id = None  # type: "string"
    strings = None  # type: "vector<languagePackString>"


class updateConnectionState(Type):
    # The connection state has changed @state The new connection state

    state = None  # type: "ConnectionState"


class updateTermsOfService(Type):
    # New terms of service must be accepted by the user.
    # If the terms of service are declined, then the deleteAccount
    # method should be called with the reason "Decline ToS update"
    # @terms_of_service_id Identifier of the terms of service @terms_of_service The new terms of service

    terms_of_service_id = None  # type: "string"
    terms_of_service = None  # type: "termsOfService"


class updateNewInlineQuery(Type):
    # A new incoming inline query; for bots only @id Unique
    # query identifier @sender_user_id Identifier of the user who sent the
    # query @user_location User location, provided by the client; may be
    # null @query Text of the query @offset Offset of the
    # first entry to return

    id = None  # type: "int64"
    sender_user_id = None  # type: "int32"
    user_location = None  # type: "location"
    query = None  # type: "string"
    offset = None  # type: "string"


class updateNewChosenInlineResult(Type):
    # The user has chosen a result of an inline query;
    # for bots only @sender_user_id Identifier of the user who sent
    # the query @user_location User location, provided by the client; may
    # be null @query Text of the query @result_id Identifier of
    # the chosen result @inline_message_id Identifier of the sent inline message, if known

    sender_user_id = None  # type: "int32"
    user_location = None  # type: "location"
    query = None  # type: "string"
    result_id = None  # type: "string"
    inline_message_id = None  # type: "string"


class updateNewCallbackQuery(Type):
    # A new incoming callback query; for bots only @id Unique
    # query identifier @sender_user_id Identifier of the user who sent the
    # query @chat_id Identifier of the chat, in which the query was sent

    id = None  # type: "int64"
    sender_user_id = None  # type: "int32"
    chat_id = None  # type: "int53"
    message_id = None  # type: "int53"
    chat_instance = None  # type: "int64"
    payload = None  # type: "CallbackQueryPayload"


class updateNewInlineCallbackQuery(Type):
    # A new incoming callback query from a message sent via
    # a bot; for bots only @id Unique query identifier @sender_user_id
    # Identifier of the user who sent the query @inline_message_id Identifier
    # of the inline message, from which the query originated

    id = None  # type: "int64"
    sender_user_id = None  # type: "int32"
    inline_message_id = None  # type: "string"
    chat_instance = None  # type: "int64"
    payload = None  # type: "CallbackQueryPayload"


class updateNewShippingQuery(Type):
    # A new incoming shipping query; for bots only. Only for
    # invoices with flexible price @id Unique query identifier @sender_user_id Identifier
    # of the user who sent the query @invoice_payload Invoice payload
    # @shipping_address User shipping address

    id = None  # type: "int64"
    sender_user_id = None  # type: "int32"
    invoice_payload = None  # type: "string"
    shipping_address = None  # type: "address"


class updateNewPreCheckoutQuery(Type):
    # A new incoming pre-checkout query; for bots only. Contains full
    # information about a checkout @id Unique query identifier @sender_user_id Identifier
    # of the user who sent the query @currency Currency for
    # the product price @total_amount Total price for the product, in
    # the minimal quantity of the currency

    id = None  # type: "int64"
    sender_user_id = None  # type: "int32"
    currency = None  # type: "string"
    total_amount = None  # type: "int53"
    invoice_payload = None  # type: "bytes"
    shipping_option_id = None  # type: "string"
    order_info = None  # type: "orderInfo"


class updateNewCustomEvent(Type):
    # A new incoming event; for bots only @event A JSON-serialized event

    event = None  # type: "string"


class updateNewCustomQuery(Type):
    # A new incoming query; for bots only @id The query
    # identifier @data JSON-serialized query data @timeout Query timeout

    id = None  # type: "int64"
    data = None  # type: "string"
    timeout = None  # type: "int32"


class testUseUpdate(Method):
    # Does nothing and ensures that the Update object is used; for testing only

    pass
