from ..factory import Method, Type


class ok(Type):
    #  object of this type is returned on a successful
    #  call for certain functions

    pass


class setTdlibParameters(Method):
    #  the parameters for TDLib initialization. Works only when the
    #  authorization state is authorizationStateWaitTdlibParameters @parameters Parameters

    parameters = None  # type: "tdlibParameters"


class checkDatabaseEncryptionKey(Method):
    #  the database encryption key for correctness. Works only when
    #  current authorization state is authorizationStateWaitEncryptionKey @encryption_key Encryption key to
    #  or set up

    encryption_key = None  # type: "bytes"


class setAuthenticationPhoneNumber(Method):
    #  the phone number of the user and sends an
    #  code to the user. Works only when the current
    #  state is authorizationStateWaitPhoneNumber

    phone_number = None  # type: "string"
    allow_flash_call = None  # type: "Bool"
    is_current_phone_number = None  # type: "Bool"


class resendAuthenticationCode(Method):
    #  an authentication code to the user. Works only when
    #  current authorization state is authorizationStateWaitCode and the next_code_type of
    #  result is not null

    pass


class checkAuthenticationCode(Method):
    #  the authentication code. Works only when the current authorization
    #  is authorizationStateWaitCode @code The verification code received via SMS,
    #  message, phone call, or flash call

    code = None  # type: "string"
    first_name = None  # type: "string"
    last_name = None  # type: "string"


class checkAuthenticationPassword(Method):
    #  the authentication password for correctness. Works only when the
    #  authorization state is authorizationStateWaitPassword @password The password to check

    password = None  # type: "string"


class requestAuthenticationPasswordRecovery(Method):
    #  to send a password recovery code to an email
    #  that was previously set up. Works only when the
    #  authorization state is authorizationStateWaitPassword

    pass


class recoverAuthenticationPassword(Method):
    #  the password with a password recovery code sent to
    #  email address that was previously set up. Works only
    #  the current authorization state is authorizationStateWaitPassword @recovery_code Recovery code to check

    recovery_code = None  # type: "string"


class checkAuthenticationBotToken(Method):
    #  the authentication token of a bot; to log in
    #  a bot. Works only when the current authorization state
    #  authorizationStateWaitPhoneNumber. Can be used instead of setAuthenticationPhoneNumber and checkAuthenticationCode
    #  log in @token The bot token

    token = None  # type: "string"


class logOut(Method):
    #  the TDLib instance after a proper logout. Requires an
    #  network connection. All local data will be destroyed. After
    #  logout completes, updateAuthorizationState with authorizationStateClosed will be sent

    pass


class close(Method):
    #  the TDLib instance. All databases will be flushed to
    #  and properly closed. After the close completes, updateAuthorizationState with
    #  will be sent

    pass


class destroy(Method):
    #  the TDLib instance, destroying all local data without a
    #  logout. The current user session will remain in the
    #  of all active sessions. All local data will be
    #  After the destruction completes updateAuthorizationState with authorizationStateClosed will be

    pass


class setDatabaseEncryptionKey(Method):
    #  the database encryption key. Usually the encryption key is
    #  changed and is stored in some OS keychain @new_encryption_key New encryption key

    new_encryption_key = None  # type: "bytes"


class processDcUpdate(Method):
    #  a DC_UPDATE push service notification. Can be called before
    #  @dc Value of the "dc" parameter of the notification
    #  Value of the "addr" parameter of the notification

    dc = None  # type: "string"
    addr = None  # type: "string"


class removeTopChat(Method):
    #  a chat from the list of frequently used chats.
    #  only if the chat info database is enabled @category
    #  of frequently used chats @chat_id Chat identifier

    category = None  # type: "TopChatCategory"
    chat_id = None  # type: "int53"


class addRecentlyFoundChat(Method):
    #  a chat to the list of recently found chats.
    #  chat is added to the beginning of the list.
    #  the chat is already in the list, it will
    #  removed from the list first @chat_id Identifier of the chat to add

    chat_id = None  # type: "int53"


class removeRecentlyFoundChat(Method):
    #  a chat from the list of recently found chats
    #  Identifier of the chat to be removed

    chat_id = None  # type: "int53"


class clearRecentlyFoundChats(Method):
    #  the list of recently found chats

    pass


class deleteChatHistory(Method):
    #  all messages in the chat only for the user.
    #  be used in channels and public supergroups @chat_id Chat
    #  @remove_from_chat_list Pass true if the chat should be removed
    #  the chats list

    chat_id = None  # type: "int53"
    remove_from_chat_list = None  # type: "Bool"


class sendChatScreenshotTakenNotification(Method):
    #  a notification about a screenshot taken in a chat.
    #  only in private and secret chats @chat_id Chat identifier

    chat_id = None  # type: "int53"


class deleteMessages(Method):
    #  messages @chat_id Chat identifier @message_ids Identifiers of the messages
    #  be deleted @revoke Pass true to try to delete
    #  messages for all chat members (may fail if messages
    #  too old). Always true for supergroups, channels and secret

    chat_id = None  # type: "int53"
    message_ids = None  # type: "vector<int53>"
    revoke = None  # type: "Bool"


class deleteChatMessagesFromUser(Method):
    #  all messages sent by the specified user to a
    #  Supported only in supergroups; requires can_delete_messages administrator privileges @chat_id
    #  identifier @user_id User identifier

    chat_id = None  # type: "int53"
    user_id = None  # type: "int32"


class editInlineMessageText(Method):
    #  the text of an inline text or game message
    #  via a bot; for bots only @inline_message_id Inline message
    #  @reply_markup The new message reply markup @input_message_content New text
    #  of the message. Should be of type InputMessageText

    inline_message_id = None  # type: "string"
    reply_markup = None  # type: "ReplyMarkup"
    input_message_content = None  # type: "InputMessageContent"


class editInlineMessageLiveLocation(Method):
    #  the content of a live location in an inline
    #  sent via a bot; for bots only @inline_message_id Inline
    #  identifier @reply_markup The new message reply markup @location New
    #  content of the message; may be null. Pass null
    #  stop sharing the live location

    inline_message_id = None  # type: "string"
    reply_markup = None  # type: "ReplyMarkup"
    location = None  # type: "location"


class editInlineMessageMedia(Method):
    #  the content of a message with an animation, an
    #  a document, a photo or a video in an
    #  message sent via a bot; for bots only @inline_message_id Inline message identifier

    inline_message_id = None  # type: "string"
    reply_markup = None  # type: "ReplyMarkup"
    input_message_content = None  # type: "InputMessageContent"


class editInlineMessageCaption(Method):
    #  the caption of an inline message sent via a
    #  for bots only @inline_message_id Inline message identifier @reply_markup The
    #  message reply markup @caption New message content caption; 0-GetOption("message_caption_length_max")

    inline_message_id = None  # type: "string"
    reply_markup = None  # type: "ReplyMarkup"
    caption = None  # type: "formattedText"


class editInlineMessageReplyMarkup(Method):
    #  the reply markup of an inline message sent via
    #  bot; for bots only @inline_message_id Inline message identifier @reply_markup
    #  new message reply markup

    inline_message_id = None  # type: "string"
    reply_markup = None  # type: "ReplyMarkup"


class answerInlineQuery(Method):
    #  the result of an inline query; for bots only
    #  Identifier of the inline query @is_personal True, if the
    #  of the query can be cached for the specified

    inline_query_id = None  # type: "int64"
    is_personal = None  # type: "Bool"
    results = None  # type: "vector<InputInlineQueryResult>"
    cache_time = None  # type: "int32"
    next_offset = None  # type: "string"
    switch_pm_text = None  # type: "string"
    switch_pm_parameter = None  # type: "string"


class answerCallbackQuery(Method):
    #  the result of a callback query; for bots only
    #  Identifier of the callback query @text Text of the
    #  @show_alert If true, an alert should be shown to
    #  user instead of a toast notification @url URL to
    #  opened @cache_time Time during which the result of the
    #  can be cached, in seconds

    callback_query_id = None  # type: "int64"
    text = None  # type: "string"
    show_alert = None  # type: "Bool"
    url = None  # type: "string"
    cache_time = None  # type: "int32"


class answerShippingQuery(Method):
    #  the result of a shipping query; for bots only
    #  Identifier of the shipping query @shipping_options Available shipping options
    #  An error message, empty on success

    shipping_query_id = None  # type: "int64"
    shipping_options = None  # type: "vector<shippingOption>"
    error_message = None  # type: "string"


class answerPreCheckoutQuery(Method):
    #  the result of a pre-checkout query; for bots only
    #  Identifier of the pre-checkout query @error_message An error message, empty on success

    pre_checkout_query_id = None  # type: "int64"
    error_message = None  # type: "string"


class setInlineGameScore(Method):
    #  the game score of the specified user in a
    #  for bots only @inline_message_id Inline message identifier @edit_message True,
    #  the message should be edited @user_id User identifier @score The new score

    inline_message_id = None  # type: "string"
    edit_message = None  # type: "Bool"
    user_id = None  # type: "int32"
    score = None  # type: "int32"
    force = None  # type: "Bool"


class deleteChatReplyMarkup(Method):
    #  the default reply markup from a chat. Must be
    #  after a one-time keyboard or a ForceReply reply markup
    #  been used. UpdateChatReplyMarkup will be sent if the reply
    #  will be changed @chat_id Chat identifier

    chat_id = None  # type: "int53"
    message_id = None  # type: "int53"


class sendChatAction(Method):
    #  a notification about user activity in a chat @chat_id
    #  identifier @action The action description

    chat_id = None  # type: "int53"
    action = None  # type: "ChatAction"


class openChat(Method):
    #  method should be called if the chat is opened
    #  the user. Many useful activities depend on the chat
    #  opened or closed (e.g., in supergroups and channels all
    #  are received only for opened chats) @chat_id Chat identifier

    chat_id = None  # type: "int53"


class closeChat(Method):
    #  method should be called if the chat is closed
    #  the user. Many useful activities depend on the chat
    #  opened or closed @chat_id Chat identifier

    chat_id = None  # type: "int53"


class viewMessages(Method):
    #  method should be called if messages are being viewed
    #  the user. Many useful activities depend on whether the
    #  are currently being viewed or not (e.g., marking messages
    #  read, incrementing a view counter, updating a view counter,
    #  deleted messages in supergroups and channels) @chat_id Chat identifier
    #  The identifiers of the messages being viewed

    chat_id = None  # type: "int53"
    message_ids = None  # type: "vector<int53>"
    force_read = None  # type: "Bool"


class openMessageContent(Method):
    #  method should be called if the message content has
    #  opened (e.g., the user has opened a photo, video,
    #  location or venue, or has listened to an audio
    #  or voice note message). An updateMessageContentOpened update will be
    #  if something has changed @chat_id Chat identifier of the
    #  @message_id Identifier of the message with the opened content

    chat_id = None  # type: "int53"
    message_id = None  # type: "int53"


class readAllChatMentions(Method):
    #  all mentions in a chat as read @chat_id Chat

    chat_id = None  # type: "int53"


class setChatTitle(Method):
    #  the chat title. Supported only for basic groups, supergroups
    #  channels. Requires administrator rights in basic groups and the
    #  administrator rights in supergroups and channels. The title will
    #  be changed until the request to the server has been completed

    chat_id = None  # type: "int53"
    title = None  # type: "string"


class setChatPhoto(Method):
    #  the photo of a chat. Supported only for basic
    #  supergroups and channels. Requires administrator rights in basic groups
    #  the appropriate administrator rights in supergroups and channels. The
    #  will not be changed before request to the server has been completed

    chat_id = None  # type: "int53"
    photo = None  # type: "InputFile"


class setChatDraftMessage(Method):
    #  the draft message in a chat @chat_id Chat identifier
    #  New draft message; may be null

    chat_id = None  # type: "int53"
    draft_message = None  # type: "draftMessage"


class setChatNotificationSettings(Method):
    #  the notification settings of a chat @chat_id Chat identifier
    #  New notification settings for the chat

    chat_id = None  # type: "int53"
    notification_settings = None  # type: "chatNotificationSettings"


class toggleChatIsPinned(Method):
    #  the pinned state of a chat. You can pin
    #  to GetOption("pinned_chat_count_max") non-secret chats and the same number of
    #  chats @chat_id Chat identifier @is_pinned New value of is_pinned

    chat_id = None  # type: "int53"
    is_pinned = None  # type: "Bool"


class toggleChatIsMarkedAsUnread(Method):
    #  the marked as unread state of a chat @chat_id
    #  identifier @is_marked_as_unread New value of is_marked_as_unread

    chat_id = None  # type: "int53"
    is_marked_as_unread = None  # type: "Bool"


class toggleChatDefaultDisableNotification(Method):
    #  the value of the default disable_notification parameter, used when
    #  message is sent to a chat @chat_id Chat identifier
    #  New value of default_disable_notification

    chat_id = None  # type: "int53"
    default_disable_notification = None  # type: "Bool"


class setChatClientData(Method):
    #  client data associated with a chat @chat_id Chat identifier
    #  New value of client_data

    chat_id = None  # type: "int53"
    client_data = None  # type: "string"


class joinChat(Method):
    #  current user as a new member to a chat.
    #  and secret chats can't be joined using this method @chat_id Chat identifier

    chat_id = None  # type: "int53"


class leaveChat(Method):
    #  current user from chat members. Private and secret chats
    #  be left using this method @chat_id Chat identifier

    chat_id = None  # type: "int53"


class addChatMember(Method):
    #  a new member to a chat. Members can't be
    #  to private or secret chats. Members will not be
    #  until the chat state has been synchronized with the

    chat_id = None  # type: "int53"
    user_id = None  # type: "int32"
    forward_limit = None  # type: "int32"


class addChatMembers(Method):
    #  multiple new members to a chat. Currently this option
    #  only available for supergroups and channels. This option can't
    #  used to join a chat. Members can't be added
    #  a channel if it has more than 200 members.
    #  will not be added until the chat state has
    #  synchronized with the server

    chat_id = None  # type: "int53"
    user_ids = None  # type: "vector<int32>"


class setChatMemberStatus(Method):
    #  the status of a chat member, needs appropriate privileges.
    #  function is currently not suitable for adding new members
    #  the chat; instead, use addChatMember. The chat member status
    #  not be changed until it has been synchronized with the server

    chat_id = None  # type: "int53"
    user_id = None  # type: "int32"
    status = None  # type: "ChatMemberStatus"


class clearAllDraftMessages(Method):
    #  draft messages in all chats @exclude_secret_chats If true, local
    #  messages in secret chats will not be cleared

    exclude_secret_chats = None  # type: "Bool"


class setScopeNotificationSettings(Method):
    #  notification settings for chats of a given type @scope
    #  of chats for which to change the notification settings
    #  The new notification settings for the given scope

    scope = None  # type: "NotificationSettingsScope"
    notification_settings = None  # type: "scopeNotificationSettings"


class resetAllNotificationSettings(Method):
    #  all notification settings to their default values. By default,
    #  chats are unmuted, the sound is set to "default"
    #  message previews are shown

    pass


class setPinnedChats(Method):
    #  the order of pinned chats @chat_ids The new list of pinned chats

    chat_ids = None  # type: "vector<int53>"


class cancelDownloadFile(Method):
    #  the downloading of a file. If a file has
    #  been downloaded, does nothing @file_id Identifier of a file
    #  stop downloading @only_if_pending Pass true to stop downloading only
    #  it hasn't been started, i.e. request hasn't been sent to server

    file_id = None  # type: "int32"
    only_if_pending = None  # type: "Bool"


class cancelUploadFile(Method):
    #  the uploading of a file. Supported only for files
    #  by using uploadFile. For other files the behavior is
    #  @file_id Identifier of the file to stop uploading

    file_id = None  # type: "int32"


class setFileGenerationProgress(Method):
    #  next part of a file was generated

    generation_id = None  # type: "int64"
    expected_size = None  # type: "int32"
    local_prefix_size = None  # type: "int32"


class finishFileGeneration(Method):
    #  the file generation

    generation_id = None  # type: "int64"
    error = None  # type: "error"


class deleteFile(Method):
    #  a file from the TDLib file cache @file_id Identifier
    #  the file to delete

    file_id = None  # type: "int32"


class acceptCall(Method):
    #  an incoming call @call_id Call identifier @protocol Description of
    #  call protocols supported by the client

    call_id = None  # type: "int32"
    protocol = None  # type: "callProtocol"


class discardCall(Method):
    #  a call @call_id Call identifier @is_disconnected True, if the
    #  was disconnected @duration The call duration, in seconds @connection_id
    #  of the connection used during the call

    call_id = None  # type: "int32"
    is_disconnected = None  # type: "Bool"
    duration = None  # type: "int32"
    connection_id = None  # type: "int64"


class sendCallRating(Method):
    #  a call rating @call_id Call identifier @rating Call rating;
    #  @comment An optional user comment if the rating is less than 5

    call_id = None  # type: "int32"
    rating = None  # type: "int32"
    comment = None  # type: "string"


class sendCallDebugInformation(Method):
    #  debug information for a call @call_id Call identifier @debug_information
    #  information in application-specific format

    call_id = None  # type: "int32"
    debug_information = None  # type: "string"


class blockUser(Method):
    #  a user to the blacklist @user_id User identifier

    user_id = None  # type: "int32"


class unblockUser(Method):
    #  a user from the blacklist @user_id User identifier

    user_id = None  # type: "int32"


class removeContacts(Method):
    #  users from the contacts list @user_ids Identifiers of users to be deleted

    user_ids = None  # type: "vector<int32>"


class clearImportedContacts(Method):
    #  all imported contacts, contacts list remains unchanged

    pass


class changeStickerSet(Method):
    #  or activates/archives a sticker set @set_id Identifier of the
    #  set @is_installed The new value of is_installed @is_archived The
    #  value of is_archived. A sticker set can't be installed and archived simultaneously

    set_id = None  # type: "int64"
    is_installed = None  # type: "Bool"
    is_archived = None  # type: "Bool"


class viewTrendingStickerSets(Method):
    #  the server that some trending sticker sets have been
    #  by the user @sticker_set_ids Identifiers of viewed trending sticker

    sticker_set_ids = None  # type: "vector<int64>"


class reorderInstalledStickerSets(Method):
    #  the order of installed sticker sets @is_masks Pass true
    #  change the order of mask sticker sets; pass false
    #  change the order of ordinary sticker sets @sticker_set_ids Identifiers
    #  installed sticker sets in the new correct order

    is_masks = None  # type: "Bool"
    sticker_set_ids = None  # type: "vector<int64>"


class removeRecentSticker(Method):
    #  a sticker from the list of recently used stickers
    #  Pass true to remove the sticker from the list
    #  stickers recently attached to photo or video files; pass
    #  to remove the sticker from the list of recently
    #  stickers @sticker Sticker file to delete

    is_attached = None  # type: "Bool"
    sticker = None  # type: "InputFile"


class clearRecentStickers(Method):
    #  the list of recently used stickers @is_attached Pass true
    #  clear the list of stickers recently attached to photo
    #  video files; pass false to clear the list of recently sent stickers

    is_attached = None  # type: "Bool"


class addFavoriteSticker(Method):
    #  a new sticker to the list of favorite stickers.
    #  new sticker is added to the top of the
    #  If the sticker was already in the list, it
    #  removed from the list first. Only stickers belonging to
    #  sticker set can be added to this list

    sticker = None  # type: "InputFile"


class removeFavoriteSticker(Method):
    #  a sticker from the list of favorite stickers @sticker
    #  file to delete from the list

    sticker = None  # type: "InputFile"


class addSavedAnimation(Method):
    #  adds a new animation to the list of saved
    #  The new animation is added to the beginning of
    #  list. If the animation was already in the list,
    #  is removed first. Only non-secret video animations with MIME
    #  "video/mp4" can be added to the list

    animation = None  # type: "InputFile"


class removeSavedAnimation(Method):
    #  an animation from the list of saved animations @animation
    #  file to be removed

    animation = None  # type: "InputFile"


class removeRecentHashtag(Method):
    #  a hashtag from the list of recently used hashtags
    #  Hashtag to delete

    hashtag = None  # type: "string"


class setProfilePhoto(Method):
    #  a new profile photo for the current user. If
    #  changes, updateUser will be sent @photo Profile photo to
    #  inputFileId and inputFileRemote may still be unsupported

    photo = None  # type: "InputFile"


class deleteProfilePhoto(Method):
    #  a profile photo. If something changes, updateUser will be
    #  @profile_photo_id Identifier of the profile photo to delete

    profile_photo_id = None  # type: "int64"


class setName(Method):
    #  the first and last name of the current user.
    #  something changes, updateUser will be sent @first_name The new
    #  of the first name for the user; 1-255 characters
    #  The new value of the optional last name for
    #  user; 0-255 characters

    first_name = None  # type: "string"
    last_name = None  # type: "string"


class setBio(Method):
    #  the bio of the current user @bio The new
    #  of the user bio; 0-70 characters without line feeds

    bio = None  # type: "string"


class setUsername(Method):
    #  the username of the current user. If something changes,
    #  will be sent @username The new value of the
    #  Use an empty string to remove the username

    username = None  # type: "string"


class checkChangePhoneNumberCode(Method):
    #  the authentication code sent to confirm a new phone
    #  of the user @code Verification code received by SMS,
    #  call or flash call

    code = None  # type: "string"


class terminateSession(Method):
    #  a session of the current user @session_id Session identifier

    session_id = None  # type: "int64"


class terminateAllOtherSessions(Method):
    #  all other sessions of the current user

    pass


class disconnectWebsite(Method):
    #  website from the current user's Telegram account @website_id Website

    website_id = None  # type: "int64"


class disconnectAllWebsites(Method):
    #  all websites from the current user's Telegram account

    pass


class toggleBasicGroupAdministrators(Method):
    #  the "All members are admins" setting in basic groups;
    #  creator privileges in the group @basic_group_id Identifier of the
    #  group @everyone_is_administrator New value of everyone_is_administrator

    basic_group_id = None  # type: "int32"
    everyone_is_administrator = None  # type: "Bool"


class setSupergroupUsername(Method):
    #  the username of a supergroup or channel, requires creator
    #  in the supergroup or channel @supergroup_id Identifier of the
    #  or channel @username New value of the username. Use
    #  empty string to remove the username

    supergroup_id = None  # type: "int32"
    username = None  # type: "string"


class setSupergroupStickerSet(Method):
    #  the sticker set of a supergroup; requires appropriate rights
    #  the supergroup @supergroup_id Identifier of the supergroup @sticker_set_id New
    #  of the supergroup sticker set identifier. Use 0 to
    #  the supergroup sticker set

    supergroup_id = None  # type: "int32"
    sticker_set_id = None  # type: "int64"


class toggleSupergroupInvites(Method):
    #  whether all members of a supergroup can add new
    #  requires appropriate administrator rights in the supergroup. @supergroup_id Identifier
    #  the supergroup @anyone_can_invite New value of anyone_can_invite

    supergroup_id = None  # type: "int32"
    anyone_can_invite = None  # type: "Bool"


class toggleSupergroupSignMessages(Method):
    #  sender signatures messages sent in a channel; requires appropriate
    #  rights in the channel. @supergroup_id Identifier of the channel
    #  New value of sign_messages

    supergroup_id = None  # type: "int32"
    sign_messages = None  # type: "Bool"


class toggleSupergroupIsAllHistoryAvailable(Method):
    #  whether the message history of a supergroup is available
    #  new members; requires appropriate administrator rights in the supergroup.
    #  The identifier of the supergroup @is_all_history_available The new value of is_all_history_available

    supergroup_id = None  # type: "int32"
    is_all_history_available = None  # type: "Bool"


class setSupergroupDescription(Method):
    #  information about a supergroup or channel; requires appropriate administrator
    #  @supergroup_id Identifier of the supergroup or channel @param_description New
    #  or channel description; 0-255 characters

    supergroup_id = None  # type: "int32"
    description = None  # type: "string"


class pinSupergroupMessage(Method):
    #  a message in a supergroup or channel; requires appropriate
    #  rights in the supergroup or channel @supergroup_id Identifier of
    #  supergroup or channel @message_id Identifier of the new pinned
    #  @disable_notification True, if there should be no notification about the pinned message

    supergroup_id = None  # type: "int32"
    message_id = None  # type: "int53"
    disable_notification = None  # type: "Bool"


class unpinSupergroupMessage(Method):
    #  the pinned message from a supergroup or channel; requires
    #  administrator rights in the supergroup or channel @supergroup_id Identifier
    #  the supergroup or channel

    supergroup_id = None  # type: "int32"


class reportSupergroupSpam(Method):
    #  some messages from a user in a supergroup as
    #  requires administrator rights in the supergroup @supergroup_id Supergroup identifier
    #  User identifier @message_ids Identifiers of messages sent in the
    #  by the user. This list must be non-empty

    supergroup_id = None  # type: "int32"
    user_id = None  # type: "int32"
    message_ids = None  # type: "vector<int53>"


class deleteSupergroup(Method):
    #  a supergroup or channel along with all messages in
    #  corresponding chat. This will release the supergroup or channel
    #  and remove all members; requires creator privileges in the
    #  or channel. Chats with more than 1000 members can't
    #  deleted using this method @supergroup_id Identifier of the supergroup or channel

    supergroup_id = None  # type: "int32"


class closeSecretChat(Method):
    #  a secret chat, effectively transfering its state to secretChatStateClosed
    #  Secret chat identifier

    secret_chat_id = None  # type: "int32"


class deleteSavedOrderInfo(Method):
    #  saved order info

    pass


class deleteSavedCredentials(Method):
    #  saved credentials for all payment provider bots

    pass


class setCustomLanguagePack(Method):
    #  or changes a custom language pack to the current
    #  target @info Information about the language pack. Language pack
    #  must start with 'X', consist only of English letters,
    #  and hyphens, and must not exceed 64 characters @strings
    #  of the new language pack

    info = None  # type: "languagePackInfo"
    strings = None  # type: "vector<languagePackString>"


class editCustomLanguagePackInfo(Method):
    #  information about a custom language pack in the current
    #  target @info New information about the custom language pack

    info = None  # type: "languagePackInfo"


class setCustomLanguagePackString(Method):
    #  edits or deletes a string in a custom language
    #  @language_pack_id Identifier of a previously added custom language pack
    #  the current localization target @new_string New language pack string

    language_pack_id = None  # type: "string"
    new_string = None  # type: "languagePackString"


class deleteLanguagePack(Method):
    #  all information about a language pack in the current
    #  target. The language pack that is currently in use
    #  be deleted @language_pack_id Identifier of the language pack to

    language_pack_id = None  # type: "string"


class registerDevice(Method):
    #  the currently used device for receiving push notifications @device_token
    #  token @other_user_ids List of at most 100 user identifiers
    #  other users currently using the client

    device_token = None  # type: "DeviceToken"
    other_user_ids = None  # type: "vector<int32>"


class setUserPrivacySettingRules(Method):
    #  user privacy settings @setting The privacy setting @rules The new privacy rules

    setting = None  # type: "UserPrivacySetting"
    rules = None  # type: "userPrivacySettingRules"


class setOption(Method):
    #  the value of an option. (Check the list of
    #  options on https://core.telegram.org/tdlib/options.) Only writable options can be set.
    #  be called before authorization

    name = None  # type: "string"
    value = None  # type: "OptionValue"


class setAccountTtl(Method):
    #  the period of inactivity after which the account of
    #  current user will automatically be deleted @ttl New account

    ttl = None  # type: "accountTtl"


class deleteAccount(Method):
    #  the account of the current user, deleting all information
    #  with the user from the server. The phone number
    #  the account can be used to create a new
    #  Can be called before authorization when the current authorization
    #  is authorizationStateWaitPassword @reason The reason why the account was deleted; optional

    reason = None  # type: "string"


class changeChatReportSpamState(Method):
    #  to let the server know whether a chat is
    #  or not. Can be used only if ChatReportSpamState.can_report_spam is
    #  After this request, ChatReportSpamState.can_report_spam becomes false forever @chat_id Chat
    #  @is_spam_chat If true, the chat will be reported as
    #  otherwise it will be marked as not spam

    chat_id = None  # type: "int53"
    is_spam_chat = None  # type: "Bool"


class reportChat(Method):
    #  a chat to the Telegram moderators. Supported only for
    #  channels, or private chats with bots, since other chats
    #  be checked by moderators @chat_id Chat identifier @reason The
    #  for reporting the chat @message_ids Identifiers of reported messages, if any

    chat_id = None  # type: "int53"
    reason = None  # type: "ChatReportReason"
    message_ids = None  # type: "vector<int53>"


class setNetworkType(Method):
    #  the current network type. Can be called before authorization.
    #  this method forces all network connections to reopen, mitigating
    #  delay in switching between different networks, so it should
    #  called whenever the network is changed, even if the
    #  type remains the same.

    type = None  # type: "NetworkType"


class addNetworkStatistics(Method):
    #  the specified data to data usage statistics. Can be
    #  before authorization @entry The network statistics entry with the
    #  to be added to statistics

    entry = None  # type: "NetworkStatisticsEntry"


class resetNetworkStatistics(Method):
    #  all network data usage statistics to zero. Can be called before authorization

    pass


class deletePassportElement(Method):
    #  a Telegram Passport element @type Element type

    type = None  # type: "PassportElementType"


class setPassportElementErrors(Method):
    #  the user that some of the elements in their
    #  Passport contain errors; for bots only. The user will
    #  be able to resend the elements, until the errors
    #  fixed @user_id User identifier @errors The errors

    user_id = None  # type: "int32"
    errors = None  # type: "vector<inputPassportElementError>"


class checkPhoneNumberVerificationCode(Method):
    #  the phone number verification code for Telegram Passport @code Verification code

    code = None  # type: "string"


class checkEmailAddressVerificationCode(Method):
    #  the email address verification code for Telegram Passport @code Verification code

    code = None  # type: "string"


class sendPassportAuthorizationForm(Method):
    #  a Telegram Passport authorization form, effectively sharing data with
    #  service @autorization_form_id Authorization form identifier @types Types of Telegram
    #  elements chosen by user to complete the authorization form

    autorization_form_id = None  # type: "int32"
    types = None  # type: "vector<PassportElementType>"


class checkPhoneNumberConfirmationCode(Method):
    #  phone number confirmation code @code The phone number confirmation

    code = None  # type: "string"


class setBotUpdatesStatus(Method):
    #  the server about the number of pending bot updates
    #  they haven't been processed for a long time; for
    #  only @pending_update_count The number of pending updates @error_message The last error message

    pending_update_count = None  # type: "int32"
    error_message = None  # type: "string"


class setStickerPositionInSet(Method):
    #  the position of a sticker in the set to
    #  it belongs; for bots only. The sticker set must
    #  been created by the bot @sticker Sticker @position New
    #  of the sticker in the set, zero-based

    sticker = None  # type: "InputFile"
    position = None  # type: "int32"


class removeStickerFromSet(Method):
    #  a sticker from the set to which it belongs;
    #  bots only. The sticker set must have been created
    #  the bot @sticker Sticker

    sticker = None  # type: "InputFile"


class acceptTermsOfService(Method):
    #  Telegram terms of services @terms_of_service_id Terms of service identifier

    terms_of_service_id = None  # type: "string"


class answerCustomQuery(Method):
    #  a custom query; for bots only @custom_query_id Identifier of
    #  custom query @data JSON-serialized answer to the query

    custom_query_id = None  # type: "int64"
    data = None  # type: "string"


class setAlarm(Method):
    #  after a specified amount of time has passed. Can
    #  called before authorization. Can be called before initialization @seconds
    #  of seconds before the function returns

    seconds = None  # type: "double"


class enableProxy(Method):
    #  a proxy. Only one proxy can be enabled at
    #  time. Can be called before authorization @proxy_id Proxy identifier

    proxy_id = None  # type: "int32"


class disableProxy(Method):
    #  the currently enabled proxy. Can be called before authorization

    pass


class removeProxy(Method):
    #  a proxy server. Can be called before authorization @proxy_id Proxy identifier

    proxy_id = None  # type: "int32"


class testCallEmpty(Method):
    #  nothing; for testing only

    pass


class testNetwork(Method):
    #  a simple network request to the Telegram servers; for testing only

    pass


class testGetDifference(Method):
    #  an updates.getDifference call to the Telegram servers; for testing

    pass
