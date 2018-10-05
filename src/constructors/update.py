from ..factory import Method, Type


class updateAuthorizationState(Type):
    #  user authorization state has changed @authorization_state New authorization state

    authorization_state = None  # type: "AuthorizationState"


class updateNewMessage(Type):
    #  new message was received; can also be an outgoing
    #  @message The new message @disable_notification True, if this message
    #  not generate a notification @contains_mention True, if the message
    #  a mention of the current user

    message = None  # type: "message"
    disable_notification = None  # type: "Bool"
    contains_mention = None  # type: "Bool"


class updateMessageSendAcknowledged(Type):
    #  request to send a message has reached the Telegram
    #  This doesn't mean that the message will be sent
    #  or even that the send message request will be
    #  This update will be sent only if the option
    #  is set to true. This update may be sent
    #  times for the same message

    chat_id = None  # type: "int53"
    message_id = None  # type: "int53"


class updateMessageSendSucceeded(Type):
    #  message has been successfully sent @message Information about the
    #  message. Usually only the message identifier, date, and content
    #  changed, but almost all other fields can also change
    #  The previous temporary message identifier

    message = None  # type: "message"
    old_message_id = None  # type: "int53"


class updateMessageSendFailed(Type):
    #  message failed to send. Be aware that some messages
    #  sent can be irrecoverably deleted, in which case updateDeleteMessages
    #  be received instead of this update

    message = None  # type: "message"
    old_message_id = None  # type: "int53"
    error_code = None  # type: "int32"
    error_message = None  # type: "string"


class updateMessageContent(Type):
    #  message content has changed @chat_id Chat identifier @message_id Message
    #  @new_content New message content

    chat_id = None  # type: "int53"
    message_id = None  # type: "int53"
    new_content = None  # type: "MessageContent"


class updateMessageEdited(Type):
    #  message was edited. Changes in the message content will
    #  in a separate updateMessageContent @chat_id Chat identifier @message_id Message
    #  @edit_date Point in time (Unix timestamp) when the message
    #  edited @reply_markup New message reply markup; may be null

    chat_id = None  # type: "int53"
    message_id = None  # type: "int53"
    edit_date = None  # type: "int32"
    reply_markup = None  # type: "ReplyMarkup"


class updateMessageViews(Type):
    #  view count of the message has changed @chat_id Chat
    #  @message_id Message identifier @views New value of the view

    chat_id = None  # type: "int53"
    message_id = None  # type: "int53"
    views = None  # type: "int32"


class updateMessageContentOpened(Type):
    #  message content was opened. Updates voice note messages to
    #  video note messages to "viewed" and starts the TTL
    #  for self-destructing messages @chat_id Chat identifier @message_id Message identifier

    chat_id = None  # type: "int53"
    message_id = None  # type: "int53"


class updateMessageMentionRead(Type):
    #  message with an unread mention was read @chat_id Chat
    #  @message_id Message identifier @unread_mention_count The new number of unread
    #  messages left in the chat

    chat_id = None  # type: "int53"
    message_id = None  # type: "int53"
    unread_mention_count = None  # type: "int32"


class updateNewChat(Type):
    #  new chat has been loaded/created. This update is guaranteed
    #  come before the chat identifier is returned to the
    #  The chat field changes will be reported through separate
    #  @chat The chat

    chat = None  # type: "chat"


class updateChatTitle(Type):
    #  title of a chat was changed @chat_id Chat identifier
    #  The new chat title

    chat_id = None  # type: "int53"
    title = None  # type: "string"


class updateChatPhoto(Type):
    #  chat photo was changed @chat_id Chat identifier @photo The
    #  chat photo; may be null

    chat_id = None  # type: "int53"
    photo = None  # type: "chatPhoto"


class updateChatLastMessage(Type):
    #  last message of a chat was changed. If last_message
    #  null then the last message in the chat became
    #  Some new unknown messages might be added to the
    #  in this case @chat_id Chat identifier @last_message The new
    #  message in the chat; may be null @order New
    #  of the chat order

    chat_id = None  # type: "int53"
    last_message = None  # type: "message"
    order = None  # type: "int64"


class updateChatOrder(Type):
    #  order of the chat in the chats list has
    #  Instead of this update updateChatLastMessage, updateChatIsPinned or updateChatDraftMessage might
    #  sent @chat_id Chat identifier @order New value of the

    chat_id = None  # type: "int53"
    order = None  # type: "int64"


class updateChatIsPinned(Type):
    #  chat was pinned or unpinned @chat_id Chat identifier @is_pinned
    #  value of is_pinned @order New value of the chat

    chat_id = None  # type: "int53"
    is_pinned = None  # type: "Bool"
    order = None  # type: "int64"


class updateChatIsMarkedAsUnread(Type):
    #  chat was marked as unread or was read @chat_id
    #  identifier @is_marked_as_unread New value of is_marked_as_unread

    chat_id = None  # type: "int53"
    is_marked_as_unread = None  # type: "Bool"


class updateChatIsSponsored(Type):
    #  chat's is_sponsored field has changed @chat_id Chat identifier @is_sponsored
    #  value of is_sponsored @order New value of chat order

    chat_id = None  # type: "int53"
    is_sponsored = None  # type: "Bool"
    order = None  # type: "int64"


class updateChatDefaultDisableNotification(Type):
    #  value of the default disable_notification parameter, used when a
    #  is sent to the chat, was changed @chat_id Chat
    #  @default_disable_notification The new default_disable_notification value

    chat_id = None  # type: "int53"
    default_disable_notification = None  # type: "Bool"


class updateChatReadInbox(Type):
    #  messages were read or number of unread messages has
    #  changed @chat_id Chat identifier @last_read_inbox_message_id Identifier of the last
    #  incoming message @unread_count The number of unread messages left in the chat

    chat_id = None  # type: "int53"
    last_read_inbox_message_id = None  # type: "int53"
    unread_count = None  # type: "int32"


class updateChatReadOutbox(Type):
    #  messages were read @chat_id Chat identifier @last_read_outbox_message_id Identifier of
    #  read outgoing message

    chat_id = None  # type: "int53"
    last_read_outbox_message_id = None  # type: "int53"


class updateChatUnreadMentionCount(Type):
    #  chat unread_mention_count has changed @chat_id Chat identifier @unread_mention_count The
    #  of unread mention messages left in the chat

    chat_id = None  # type: "int53"
    unread_mention_count = None  # type: "int32"


class updateChatNotificationSettings(Type):
    #  settings for a chat were changed @chat_id Chat identifier
    #  The new notification settings

    chat_id = None  # type: "int53"
    notification_settings = None  # type: "chatNotificationSettings"


class updateScopeNotificationSettings(Type):
    #  settings for some type of chats were updated @scope
    #  of chats for which notification settings were updated @notification_settings
    #  new notification settings

    scope = None  # type: "NotificationSettingsScope"
    notification_settings = None  # type: "scopeNotificationSettings"


class updateChatReplyMarkup(Type):
    #  default chat reply markup was changed. Can occur because
    #  messages with reply markup were received or because an
    #  reply markup was hidden by the user

    chat_id = None  # type: "int53"
    reply_markup_message_id = None  # type: "int53"


class updateChatDraftMessage(Type):
    #  chat draft has changed. Be aware that the update
    #  come in the currently opened chat but with old
    #  of the draft. If the user has changed the
    #  of the draft, this update shouldn't be applied @chat_id
    #  identifier @draft_message The new draft message; may be null
    #  New value of the chat order

    chat_id = None  # type: "int53"
    draft_message = None  # type: "draftMessage"
    order = None  # type: "int64"


class updateDeleteMessages(Type):
    #  messages were deleted @chat_id Chat identifier @message_ids Identifiers of the deleted messages

    chat_id = None  # type: "int53"
    message_ids = None  # type: "vector<int53>"
    is_permanent = None  # type: "Bool"
    from_cache = None  # type: "Bool"


class updateUserChatAction(Type):
    #  activity in the chat has changed @chat_id Chat identifier
    #  Identifier of a user performing an action @action The action description

    chat_id = None  # type: "int53"
    user_id = None  # type: "int32"
    action = None  # type: "ChatAction"


class updateUserStatus(Type):
    #  user went online or offline @user_id User identifier @status
    #  status of the user

    user_id = None  # type: "int32"
    status = None  # type: "UserStatus"


class updateUser(Type):
    #  data of a user has changed. This update is
    #  to come before the user identifier is returned to
    #  client @user New data about the user

    user = None  # type: "user"


class updateBasicGroup(Type):
    #  data of a basic group has changed. This update
    #  guaranteed to come before the basic group identifier is
    #  to the client @basic_group New data about the group

    basic_group = None  # type: "basicGroup"


class updateSupergroup(Type):
    #  data of a supergroup or a channel has changed.
    #  update is guaranteed to come before the supergroup identifier
    #  returned to the client @supergroup New data about the

    supergroup = None  # type: "supergroup"


class updateSecretChat(Type):
    #  data of a secret chat has changed. This update
    #  guaranteed to come before the secret chat identifier is
    #  to the client @secret_chat New data about the secret

    secret_chat = None  # type: "secretChat"


class updateUserFullInfo(Type):
    #  data from userFullInfo has been changed @user_id User identifier
    #  New full information about the user

    user_id = None  # type: "int32"
    user_full_info = None  # type: "userFullInfo"


class updateBasicGroupFullInfo(Type):
    #  data from basicGroupFullInfo has been changed @basic_group_id Identifier of
    #  basic group @basic_group_full_info New full information about the group

    basic_group_id = None  # type: "int32"
    basic_group_full_info = None  # type: "basicGroupFullInfo"


class updateSupergroupFullInfo(Type):
    #  data from supergroupFullInfo has been changed @supergroup_id Identifier of
    #  supergroup or channel @supergroup_full_info New full information about the

    supergroup_id = None  # type: "int32"
    supergroup_full_info = None  # type: "supergroupFullInfo"


class updateServiceNotification(Type):
    #  notification from the server. Upon receiving this the client
    #  show a popup with the content of the notification

    type = None  # type: "string"
    content = None  # type: "MessageContent"


class updateFile(Type):
    #  about a file was updated @file New data about the file

    file = None  # type: "file"


class updateFileGenerationStart(Type):
    #  file generation process needs to be started by the

    generation_id = None  # type: "int64"
    original_path = None  # type: "string"
    destination_path = None  # type: "string"
    conversion = None  # type: "string"


class updateFileGenerationStop(Type):
    #  generation is no longer needed @generation_id Unique identifier for the generation process

    generation_id = None  # type: "int64"


class updateCall(Type):
    #  call was created or information about a call was
    #  @call New data about a call

    call = None  # type: "call"


class updateUserPrivacySettingRules(Type):
    #  privacy setting rules have been changed @setting The privacy
    #  @rules New privacy rules

    setting = None  # type: "UserPrivacySetting"
    rules = None  # type: "userPrivacySettingRules"


class updateUnreadMessageCount(Type):
    #  of unread messages has changed. This update is sent
    #  if a message database is used @unread_count Total number
    #  unread messages @unread_unmuted_count Total number of unread messages in unmuted chats

    unread_count = None  # type: "int32"
    unread_unmuted_count = None  # type: "int32"


class updateUnreadChatCount(Type):
    #  of unread chats, i.e. with unread messages or marked
    #  unread, has changed. This update is sent only if
    #  message database is used

    unread_count = None  # type: "int32"
    unread_unmuted_count = None  # type: "int32"
    marked_as_unread_count = None  # type: "int32"
    marked_as_unread_unmuted_count = None  # type: "int32"


class updateOption(Type):
    #  option changed its value @name The option name @value
    #  new option value

    name = None  # type: "string"
    value = None  # type: "OptionValue"


class updateInstalledStickerSets(Type):
    #  list of installed sticker sets was updated @is_masks True,
    #  the list of installed mask sticker sets was updated
    #  The new list of installed ordinary sticker sets

    is_masks = None  # type: "Bool"
    sticker_set_ids = None  # type: "vector<int64>"


class updateTrendingStickerSets(Type):
    #  list of trending sticker sets was updated or some
    #  them were viewed @sticker_sets The new list of trending sticker sets

    sticker_sets = None  # type: "stickerSets"


class updateRecentStickers(Type):
    #  list of recently used stickers was updated @is_attached True,
    #  the list of stickers attached to photo or video
    #  was updated, otherwise the list of sent stickers is
    #  @sticker_ids The new list of file identifiers of recently used stickers

    is_attached = None  # type: "Bool"
    sticker_ids = None  # type: "vector<int32>"


class updateFavoriteStickers(Type):
    #  list of favorite stickers was updated @sticker_ids The new
    #  of file identifiers of favorite stickers

    sticker_ids = None  # type: "vector<int32>"


class updateSavedAnimations(Type):
    #  list of saved animations was updated @animation_ids The new
    #  of file identifiers of saved animations

    animation_ids = None  # type: "vector<int32>"


class updateLanguagePackStrings(Type):
    #  language pack strings have been updated @localization_target Localization target
    #  which the language pack belongs @language_pack_id Identifier of the
    #  language pack @strings List of changed language pack strings

    localization_target = None  # type: "string"
    language_pack_id = None  # type: "string"
    strings = None  # type: "vector<languagePackString>"


class updateConnectionState(Type):
    #  connection state has changed @state The new connection state

    state = None  # type: "ConnectionState"


class updateTermsOfService(Type):
    #  terms of service must be accepted by the user.
    #  the terms of service are declined, then the deleteAccount
    #  should be called with the reason "Decline ToS update"
    #  Identifier of the terms of service @terms_of_service The new terms of service

    terms_of_service_id = None  # type: "string"
    terms_of_service = None  # type: "termsOfService"


class updateNewInlineQuery(Type):
    #  new incoming inline query; for bots only @id Unique
    #  identifier @sender_user_id Identifier of the user who sent the
    #  @user_location User location, provided by the client; may be
    #  @query Text of the query @offset Offset of the
    #  entry to return

    id = None  # type: "int64"
    sender_user_id = None  # type: "int32"
    user_location = None  # type: "location"
    query = None  # type: "string"
    offset = None  # type: "string"


class updateNewChosenInlineResult(Type):
    #  user has chosen a result of an inline query;
    #  bots only @sender_user_id Identifier of the user who sent
    #  query @user_location User location, provided by the client; may
    #  null @query Text of the query @result_id Identifier of
    #  chosen result @inline_message_id Identifier of the sent inline message, if known

    sender_user_id = None  # type: "int32"
    user_location = None  # type: "location"
    query = None  # type: "string"
    result_id = None  # type: "string"
    inline_message_id = None  # type: "string"


class updateNewCallbackQuery(Type):
    #  new incoming callback query; for bots only @id Unique
    #  identifier @sender_user_id Identifier of the user who sent the
    #  @chat_id Identifier of the chat, in which the query was sent

    id = None  # type: "int64"
    sender_user_id = None  # type: "int32"
    chat_id = None  # type: "int53"
    message_id = None  # type: "int53"
    chat_instance = None  # type: "int64"
    payload = None  # type: "CallbackQueryPayload"


class updateNewInlineCallbackQuery(Type):
    #  new incoming callback query from a message sent via
    #  bot; for bots only @id Unique query identifier @sender_user_id
    #  of the user who sent the query @inline_message_id Identifier
    #  the inline message, from which the query originated

    id = None  # type: "int64"
    sender_user_id = None  # type: "int32"
    inline_message_id = None  # type: "string"
    chat_instance = None  # type: "int64"
    payload = None  # type: "CallbackQueryPayload"


class updateNewShippingQuery(Type):
    #  new incoming shipping query; for bots only. Only for
    #  with flexible price @id Unique query identifier @sender_user_id Identifier
    #  the user who sent the query @invoice_payload Invoice payload
    #  User shipping address

    id = None  # type: "int64"
    sender_user_id = None  # type: "int32"
    invoice_payload = None  # type: "string"
    shipping_address = None  # type: "address"


class updateNewPreCheckoutQuery(Type):
    #  new incoming pre-checkout query; for bots only. Contains full
    #  about a checkout @id Unique query identifier @sender_user_id Identifier
    #  the user who sent the query @currency Currency for
    #  product price @total_amount Total price for the product, in
    #  minimal quantity of the currency

    id = None  # type: "int64"
    sender_user_id = None  # type: "int32"
    currency = None  # type: "string"
    total_amount = None  # type: "int53"
    invoice_payload = None  # type: "bytes"
    shipping_option_id = None  # type: "string"
    order_info = None  # type: "orderInfo"


class updateNewCustomEvent(Type):
    #  new incoming event; for bots only @event A JSON-serialized

    event = None  # type: "string"


class updateNewCustomQuery(Type):
    #  new incoming query; for bots only @id The query
    #  @data JSON-serialized query data @timeout Query timeout

    id = None  # type: "int64"
    data = None  # type: "string"
    timeout = None  # type: "int32"


class testUseUpdate(Method):
    #  nothing and ensures that the Update object is used; for testing only

    pass
