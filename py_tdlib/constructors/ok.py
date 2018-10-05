from ..factory import Method, Type


class ok(Type):
    # An object of this type is returned on a successful
    # function call for certain functions

    pass


class setTdlibParameters(Method):
    # Sets the parameters for TDLib initialization. Works only when the
    # current authorization state is authorizationStateWaitTdlibParameters @parameters Parameters

    parameters = None  # type: "tdlibParameters"


class checkDatabaseEncryptionKey(Method):
    # Checks the database encryption key for correctness. Works only when
    # the current authorization state is authorizationStateWaitEncryptionKey @encryption_key Encryption key to
    # check or set up

    encryption_key = None  # type: "bytes"


class setAuthenticationPhoneNumber(Method):
    # Sets the phone number of the user and sends an
    # authentication code to the user. Works only when the current
    # authorization state is authorizationStateWaitPhoneNumber

    phone_number = None  # type: "string"
    allow_flash_call = None  # type: "Bool"
    is_current_phone_number = None  # type: "Bool"


class resendAuthenticationCode(Method):
    # Re-sends an authentication code to the user. Works only when
    # the current authorization state is authorizationStateWaitCode and the next_code_type of
    # the result is not null

    pass


class checkAuthenticationCode(Method):
    # Checks the authentication code. Works only when the current authorization
    # state is authorizationStateWaitCode @code The verification code received via SMS,
    # Telegram message, phone call, or flash call

    code = None  # type: "string"
    first_name = None  # type: "string"
    last_name = None  # type: "string"


class checkAuthenticationPassword(Method):
    # Checks the authentication password for correctness. Works only when the
    # current authorization state is authorizationStateWaitPassword @password The password to check

    password = None  # type: "string"


class requestAuthenticationPasswordRecovery(Method):
    # Requests to send a password recovery code to an email
    # address that was previously set up. Works only when the
    # current authorization state is authorizationStateWaitPassword

    pass


class recoverAuthenticationPassword(Method):
    # Recovers the password with a password recovery code sent to
    # an email address that was previously set up. Works only
    # when the current authorization state is authorizationStateWaitPassword @recovery_code Recovery code to check

    recovery_code = None  # type: "string"


class checkAuthenticationBotToken(Method):
    # Checks the authentication token of a bot; to log in
    # as a bot. Works only when the current authorization state
    # is authorizationStateWaitPhoneNumber. Can be used instead of setAuthenticationPhoneNumber and checkAuthenticationCode
    # to log in @token The bot token

    token = None  # type: "string"


class logOut(Method):
    # Closes the TDLib instance after a proper logout. Requires an
    # available network connection. All local data will be destroyed. After
    # the logout completes, updateAuthorizationState with authorizationStateClosed will be sent

    pass


class close(Method):
    # Closes the TDLib instance. All databases will be flushed to
    # disk and properly closed. After the close completes, updateAuthorizationState with
    # authorizationStateClosed will be sent

    pass


class destroy(Method):
    # Closes the TDLib instance, destroying all local data without a
    # proper logout. The current user session will remain in the
    # list of all active sessions. All local data will be
    # destroyed. After the destruction completes updateAuthorizationState with authorizationStateClosed will be sent

    pass


class setDatabaseEncryptionKey(Method):
    # Changes the database encryption key. Usually the encryption key is
    # never changed and is stored in some OS keychain @new_encryption_key New encryption key

    new_encryption_key = None  # type: "bytes"


class processDcUpdate(Method):
    # Handles a DC_UPDATE push service notification. Can be called before
    # authorization @dc Value of the "dc" parameter of the notification
    # @addr Value of the "addr" parameter of the notification

    dc = None  # type: "string"
    addr = None  # type: "string"


class removeTopChat(Method):
    # Removes a chat from the list of frequently used chats.
    # Supported only if the chat info database is enabled @category
    # Category of frequently used chats @chat_id Chat identifier

    category = None  # type: "TopChatCategory"
    chat_id = None  # type: "int53"


class addRecentlyFoundChat(Method):
    # Adds a chat to the list of recently found chats.
    # The chat is added to the beginning of the list.
    # If the chat is already in the list, it will
    # be removed from the list first @chat_id Identifier of the chat to add

    chat_id = None  # type: "int53"


class removeRecentlyFoundChat(Method):
    # Removes a chat from the list of recently found chats
    # @chat_id Identifier of the chat to be removed

    chat_id = None  # type: "int53"


class clearRecentlyFoundChats(Method):
    # Clears the list of recently found chats

    pass


class deleteChatHistory(Method):
    # Deletes all messages in the chat only for the user.
    # Cannot be used in channels and public supergroups @chat_id Chat
    # identifier @remove_from_chat_list Pass true if the chat should be removed
    # from the chats list

    chat_id = None  # type: "int53"
    remove_from_chat_list = None  # type: "Bool"


class sendChatScreenshotTakenNotification(Method):
    # Sends a notification about a screenshot taken in a chat.
    # Supported only in private and secret chats @chat_id Chat identifier

    chat_id = None  # type: "int53"


class deleteMessages(Method):
    # Deletes messages @chat_id Chat identifier @message_ids Identifiers of the messages
    # to be deleted @revoke Pass true to try to delete
    # outgoing messages for all chat members (may fail if messages
    # are too old). Always true for supergroups, channels and secret chats

    chat_id = None  # type: "int53"
    message_ids = None  # type: "vector<int53>"
    revoke = None  # type: "Bool"


class deleteChatMessagesFromUser(Method):
    # Deletes all messages sent by the specified user to a
    # chat. Supported only in supergroups; requires can_delete_messages administrator privileges @chat_id
    # Chat identifier @user_id User identifier

    chat_id = None  # type: "int53"
    user_id = None  # type: "int32"


class editInlineMessageText(Method):
    # Edits the text of an inline text or game message
    # sent via a bot; for bots only @inline_message_id Inline message
    # identifier @reply_markup The new message reply markup @input_message_content New text
    # content of the message. Should be of type InputMessageText

    inline_message_id = None  # type: "string"
    reply_markup = None  # type: "ReplyMarkup"
    input_message_content = None  # type: "InputMessageContent"


class editInlineMessageLiveLocation(Method):
    # Edits the content of a live location in an inline
    # message sent via a bot; for bots only @inline_message_id Inline
    # message identifier @reply_markup The new message reply markup @location New
    # location content of the message; may be null. Pass null
    # to stop sharing the live location

    inline_message_id = None  # type: "string"
    reply_markup = None  # type: "ReplyMarkup"
    location = None  # type: "location"


class editInlineMessageMedia(Method):
    # Edits the content of a message with an animation, an
    # audio, a document, a photo or a video in an
    # inline message sent via a bot; for bots only @inline_message_id Inline message identifier

    inline_message_id = None  # type: "string"
    reply_markup = None  # type: "ReplyMarkup"
    input_message_content = None  # type: "InputMessageContent"


class editInlineMessageCaption(Method):
    # Edits the caption of an inline message sent via a
    # bot; for bots only @inline_message_id Inline message identifier @reply_markup The
    # new message reply markup @caption New message content caption; 0-GetOption("message_caption_length_max") characters

    inline_message_id = None  # type: "string"
    reply_markup = None  # type: "ReplyMarkup"
    caption = None  # type: "formattedText"


class editInlineMessageReplyMarkup(Method):
    # Edits the reply markup of an inline message sent via
    # a bot; for bots only @inline_message_id Inline message identifier @reply_markup
    # The new message reply markup

    inline_message_id = None  # type: "string"
    reply_markup = None  # type: "ReplyMarkup"


class answerInlineQuery(Method):
    # Sets the result of an inline query; for bots only
    # @inline_query_id Identifier of the inline query @is_personal True, if the
    # result of the query can be cached for the specified user

    inline_query_id = None  # type: "int64"
    is_personal = None  # type: "Bool"
    results = None  # type: "vector<InputInlineQueryResult>"
    cache_time = None  # type: "int32"
    next_offset = None  # type: "string"
    switch_pm_text = None  # type: "string"
    switch_pm_parameter = None  # type: "string"


class answerCallbackQuery(Method):
    # Sets the result of a callback query; for bots only
    # @callback_query_id Identifier of the callback query @text Text of the
    # answer @show_alert If true, an alert should be shown to
    # the user instead of a toast notification @url URL to
    # be opened @cache_time Time during which the result of the
    # query can be cached, in seconds

    callback_query_id = None  # type: "int64"
    text = None  # type: "string"
    show_alert = None  # type: "Bool"
    url = None  # type: "string"
    cache_time = None  # type: "int32"


class answerShippingQuery(Method):
    # Sets the result of a shipping query; for bots only
    # @shipping_query_id Identifier of the shipping query @shipping_options Available shipping options
    # @error_message An error message, empty on success

    shipping_query_id = None  # type: "int64"
    shipping_options = None  # type: "vector<shippingOption>"
    error_message = None  # type: "string"


class answerPreCheckoutQuery(Method):
    # Sets the result of a pre-checkout query; for bots only
    # @pre_checkout_query_id Identifier of the pre-checkout query @error_message An error message, empty on success

    pre_checkout_query_id = None  # type: "int64"
    error_message = None  # type: "string"


class setInlineGameScore(Method):
    # Updates the game score of the specified user in a
    # game; for bots only @inline_message_id Inline message identifier @edit_message True,
    # if the message should be edited @user_id User identifier @score The new score

    inline_message_id = None  # type: "string"
    edit_message = None  # type: "Bool"
    user_id = None  # type: "int32"
    score = None  # type: "int32"
    force = None  # type: "Bool"


class deleteChatReplyMarkup(Method):
    # Deletes the default reply markup from a chat. Must be
    # called after a one-time keyboard or a ForceReply reply markup
    # has been used. UpdateChatReplyMarkup will be sent if the reply
    # markup will be changed @chat_id Chat identifier

    chat_id = None  # type: "int53"
    message_id = None  # type: "int53"


class sendChatAction(Method):
    # Sends a notification about user activity in a chat @chat_id
    # Chat identifier @action The action description

    chat_id = None  # type: "int53"
    action = None  # type: "ChatAction"


class openChat(Method):
    # This method should be called if the chat is opened
    # by the user. Many useful activities depend on the chat
    # being opened or closed (e.g., in supergroups and channels all
    # updates are received only for opened chats) @chat_id Chat identifier

    chat_id = None  # type: "int53"


class closeChat(Method):
    # This method should be called if the chat is closed
    # by the user. Many useful activities depend on the chat
    # being opened or closed @chat_id Chat identifier

    chat_id = None  # type: "int53"


class viewMessages(Method):
    # This method should be called if messages are being viewed
    # by the user. Many useful activities depend on whether the
    # messages are currently being viewed or not (e.g., marking messages
    # as read, incrementing a view counter, updating a view counter,
    # removing deleted messages in supergroups and channels) @chat_id Chat identifier
    # @message_ids The identifiers of the messages being viewed

    chat_id = None  # type: "int53"
    message_ids = None  # type: "vector<int53>"
    force_read = None  # type: "Bool"


class openMessageContent(Method):
    # This method should be called if the message content has
    # been opened (e.g., the user has opened a photo, video,
    # document, location or venue, or has listened to an audio
    # file or voice note message). An updateMessageContentOpened update will be
    # generated if something has changed @chat_id Chat identifier of the
    # message @message_id Identifier of the message with the opened content

    chat_id = None  # type: "int53"
    message_id = None  # type: "int53"


class readAllChatMentions(Method):
    # Marks all mentions in a chat as read @chat_id Chat identifier

    chat_id = None  # type: "int53"


class setChatTitle(Method):
    # Changes the chat title. Supported only for basic groups, supergroups
    # and channels. Requires administrator rights in basic groups and the
    # appropriate administrator rights in supergroups and channels. The title will
    # not be changed until the request to the server has been completed

    chat_id = None  # type: "int53"
    title = None  # type: "string"


class setChatPhoto(Method):
    # Changes the photo of a chat. Supported only for basic
    # groups, supergroups and channels. Requires administrator rights in basic groups
    # and the appropriate administrator rights in supergroups and channels. The
    # photo will not be changed before request to the server has been completed

    chat_id = None  # type: "int53"
    photo = None  # type: "InputFile"


class setChatDraftMessage(Method):
    # Changes the draft message in a chat @chat_id Chat identifier
    # @draft_message New draft message; may be null

    chat_id = None  # type: "int53"
    draft_message = None  # type: "draftMessage"


class setChatNotificationSettings(Method):
    # Changes the notification settings of a chat @chat_id Chat identifier
    # @notification_settings New notification settings for the chat

    chat_id = None  # type: "int53"
    notification_settings = None  # type: "chatNotificationSettings"


class toggleChatIsPinned(Method):
    # Changes the pinned state of a chat. You can pin
    # up to GetOption("pinned_chat_count_max") non-secret chats and the same number of
    # secret chats @chat_id Chat identifier @is_pinned New value of is_pinned

    chat_id = None  # type: "int53"
    is_pinned = None  # type: "Bool"


class toggleChatIsMarkedAsUnread(Method):
    # Changes the marked as unread state of a chat @chat_id
    # Chat identifier @is_marked_as_unread New value of is_marked_as_unread

    chat_id = None  # type: "int53"
    is_marked_as_unread = None  # type: "Bool"


class toggleChatDefaultDisableNotification(Method):
    # Changes the value of the default disable_notification parameter, used when
    # a message is sent to a chat @chat_id Chat identifier
    # @default_disable_notification New value of default_disable_notification

    chat_id = None  # type: "int53"
    default_disable_notification = None  # type: "Bool"


class setChatClientData(Method):
    # Changes client data associated with a chat @chat_id Chat identifier
    # @client_data New value of client_data

    chat_id = None  # type: "int53"
    client_data = None  # type: "string"


class joinChat(Method):
    # Adds current user as a new member to a chat.
    # Private and secret chats can't be joined using this method @chat_id Chat identifier

    chat_id = None  # type: "int53"


class leaveChat(Method):
    # Removes current user from chat members. Private and secret chats
    # can't be left using this method @chat_id Chat identifier

    chat_id = None  # type: "int53"


class addChatMember(Method):
    # Adds a new member to a chat. Members can't be
    # added to private or secret chats. Members will not be
    # added until the chat state has been synchronized with the server

    chat_id = None  # type: "int53"
    user_id = None  # type: "int32"
    forward_limit = None  # type: "int32"


class addChatMembers(Method):
    # Adds multiple new members to a chat. Currently this option
    # is only available for supergroups and channels. This option can't
    # be used to join a chat. Members can't be added
    # to a channel if it has more than 200 members.
    # Members will not be added until the chat state has
    # been synchronized with the server

    chat_id = None  # type: "int53"
    user_ids = None  # type: "vector<int32>"


class setChatMemberStatus(Method):
    # Changes the status of a chat member, needs appropriate privileges.
    # This function is currently not suitable for adding new members
    # to the chat; instead, use addChatMember. The chat member status
    # will not be changed until it has been synchronized with the server

    chat_id = None  # type: "int53"
    user_id = None  # type: "int32"
    status = None  # type: "ChatMemberStatus"


class clearAllDraftMessages(Method):
    # Clears draft messages in all chats @exclude_secret_chats If true, local
    # draft messages in secret chats will not be cleared

    exclude_secret_chats = None  # type: "Bool"


class setScopeNotificationSettings(Method):
    # Changes notification settings for chats of a given type @scope
    # Types of chats for which to change the notification settings
    # @notification_settings The new notification settings for the given scope

    scope = None  # type: "NotificationSettingsScope"
    notification_settings = None  # type: "scopeNotificationSettings"


class resetAllNotificationSettings(Method):
    # Resets all notification settings to their default values. By default,
    # all chats are unmuted, the sound is set to "default"
    # and message previews are shown

    pass


class setPinnedChats(Method):
    # Changes the order of pinned chats @chat_ids The new list of pinned chats

    chat_ids = None  # type: "vector<int53>"


class cancelDownloadFile(Method):
    # Stops the downloading of a file. If a file has
    # already been downloaded, does nothing @file_id Identifier of a file
    # to stop downloading @only_if_pending Pass true to stop downloading only
    # if it hasn't been started, i.e. request hasn't been sent to server

    file_id = None  # type: "int32"
    only_if_pending = None  # type: "Bool"


class cancelUploadFile(Method):
    # Stops the uploading of a file. Supported only for files
    # uploaded by using uploadFile. For other files the behavior is
    # undefined @file_id Identifier of the file to stop uploading

    file_id = None  # type: "int32"


class setFileGenerationProgress(Method):
    # The next part of a file was generated

    generation_id = None  # type: "int64"
    expected_size = None  # type: "int32"
    local_prefix_size = None  # type: "int32"


class finishFileGeneration(Method):
    # Finishes the file generation

    generation_id = None  # type: "int64"
    error = None  # type: "error"


class deleteFile(Method):
    # Deletes a file from the TDLib file cache @file_id Identifier
    # of the file to delete

    file_id = None  # type: "int32"


class acceptCall(Method):
    # Accepts an incoming call @call_id Call identifier @protocol Description of
    # the call protocols supported by the client

    call_id = None  # type: "int32"
    protocol = None  # type: "callProtocol"


class discardCall(Method):
    # Discards a call @call_id Call identifier @is_disconnected True, if the
    # user was disconnected @duration The call duration, in seconds @connection_id
    # Identifier of the connection used during the call

    call_id = None  # type: "int32"
    is_disconnected = None  # type: "Bool"
    duration = None  # type: "int32"
    connection_id = None  # type: "int64"


class sendCallRating(Method):
    # Sends a call rating @call_id Call identifier @rating Call rating;
    # 1-5 @comment An optional user comment if the rating is less than 5

    call_id = None  # type: "int32"
    rating = None  # type: "int32"
    comment = None  # type: "string"


class sendCallDebugInformation(Method):
    # Sends debug information for a call @call_id Call identifier @debug_information
    # Debug information in application-specific format

    call_id = None  # type: "int32"
    debug_information = None  # type: "string"


class blockUser(Method):
    # Adds a user to the blacklist @user_id User identifier

    user_id = None  # type: "int32"


class unblockUser(Method):
    # Removes a user from the blacklist @user_id User identifier

    user_id = None  # type: "int32"


class removeContacts(Method):
    # Removes users from the contacts list @user_ids Identifiers of users to be deleted

    user_ids = None  # type: "vector<int32>"


class clearImportedContacts(Method):
    # Clears all imported contacts, contacts list remains unchanged

    pass


class changeStickerSet(Method):
    # Installs/uninstalls or activates/archives a sticker set @set_id Identifier of the
    # sticker set @is_installed The new value of is_installed @is_archived The
    # new value of is_archived. A sticker set can't be installed and archived simultaneously

    set_id = None  # type: "int64"
    is_installed = None  # type: "Bool"
    is_archived = None  # type: "Bool"


class viewTrendingStickerSets(Method):
    # Informs the server that some trending sticker sets have been
    # viewed by the user @sticker_set_ids Identifiers of viewed trending sticker sets

    sticker_set_ids = None  # type: "vector<int64>"


class reorderInstalledStickerSets(Method):
    # Changes the order of installed sticker sets @is_masks Pass true
    # to change the order of mask sticker sets; pass false
    # to change the order of ordinary sticker sets @sticker_set_ids Identifiers
    # of installed sticker sets in the new correct order

    is_masks = None  # type: "Bool"
    sticker_set_ids = None  # type: "vector<int64>"


class removeRecentSticker(Method):
    # Removes a sticker from the list of recently used stickers
    # @is_attached Pass true to remove the sticker from the list
    # of stickers recently attached to photo or video files; pass
    # false to remove the sticker from the list of recently
    # sent stickers @sticker Sticker file to delete

    is_attached = None  # type: "Bool"
    sticker = None  # type: "InputFile"


class clearRecentStickers(Method):
    # Clears the list of recently used stickers @is_attached Pass true
    # to clear the list of stickers recently attached to photo
    # or video files; pass false to clear the list of recently sent stickers

    is_attached = None  # type: "Bool"


class addFavoriteSticker(Method):
    # Adds a new sticker to the list of favorite stickers.
    # The new sticker is added to the top of the
    # list. If the sticker was already in the list, it
    # is removed from the list first. Only stickers belonging to
    # a sticker set can be added to this list

    sticker = None  # type: "InputFile"


class removeFavoriteSticker(Method):
    # Removes a sticker from the list of favorite stickers @sticker
    # Sticker file to delete from the list

    sticker = None  # type: "InputFile"


class addSavedAnimation(Method):
    # Manually adds a new animation to the list of saved
    # animations. The new animation is added to the beginning of
    # the list. If the animation was already in the list,
    # it is removed first. Only non-secret video animations with MIME
    # type "video/mp4" can be added to the list

    animation = None  # type: "InputFile"


class removeSavedAnimation(Method):
    # Removes an animation from the list of saved animations @animation
    # Animation file to be removed

    animation = None  # type: "InputFile"


class removeRecentHashtag(Method):
    # Removes a hashtag from the list of recently used hashtags
    # @hashtag Hashtag to delete

    hashtag = None  # type: "string"


class setProfilePhoto(Method):
    # Uploads a new profile photo for the current user. If
    # something changes, updateUser will be sent @photo Profile photo to
    # set. inputFileId and inputFileRemote may still be unsupported

    photo = None  # type: "InputFile"


class deleteProfilePhoto(Method):
    # Deletes a profile photo. If something changes, updateUser will be
    # sent @profile_photo_id Identifier of the profile photo to delete

    profile_photo_id = None  # type: "int64"


class setName(Method):
    # Changes the first and last name of the current user.
    # If something changes, updateUser will be sent @first_name The new
    # value of the first name for the user; 1-255 characters
    # @last_name The new value of the optional last name for
    # the user; 0-255 characters

    first_name = None  # type: "string"
    last_name = None  # type: "string"


class setBio(Method):
    # Changes the bio of the current user @bio The new
    # value of the user bio; 0-70 characters without line feeds

    bio = None  # type: "string"


class setUsername(Method):
    # Changes the username of the current user. If something changes,
    # updateUser will be sent @username The new value of the
    # username. Use an empty string to remove the username

    username = None  # type: "string"


class checkChangePhoneNumberCode(Method):
    # Checks the authentication code sent to confirm a new phone
    # number of the user @code Verification code received by SMS,
    # phone call or flash call

    code = None  # type: "string"


class terminateSession(Method):
    # Terminates a session of the current user @session_id Session identifier

    session_id = None  # type: "int64"


class terminateAllOtherSessions(Method):
    # Terminates all other sessions of the current user

    pass


class disconnectWebsite(Method):
    # Disconnects website from the current user's Telegram account @website_id Website identifier

    website_id = None  # type: "int64"


class disconnectAllWebsites(Method):
    # Disconnects all websites from the current user's Telegram account

    pass


class toggleBasicGroupAdministrators(Method):
    # Toggles the "All members are admins" setting in basic groups;
    # requires creator privileges in the group @basic_group_id Identifier of the
    # basic group @everyone_is_administrator New value of everyone_is_administrator

    basic_group_id = None  # type: "int32"
    everyone_is_administrator = None  # type: "Bool"


class setSupergroupUsername(Method):
    # Changes the username of a supergroup or channel, requires creator
    # privileges in the supergroup or channel @supergroup_id Identifier of the
    # supergroup or channel @username New value of the username. Use
    # an empty string to remove the username

    supergroup_id = None  # type: "int32"
    username = None  # type: "string"


class setSupergroupStickerSet(Method):
    # Changes the sticker set of a supergroup; requires appropriate rights
    # in the supergroup @supergroup_id Identifier of the supergroup @sticker_set_id New
    # value of the supergroup sticker set identifier. Use 0 to
    # remove the supergroup sticker set

    supergroup_id = None  # type: "int32"
    sticker_set_id = None  # type: "int64"


class toggleSupergroupInvites(Method):
    # Toggles whether all members of a supergroup can add new
    # members; requires appropriate administrator rights in the supergroup. @supergroup_id Identifier
    # of the supergroup @anyone_can_invite New value of anyone_can_invite

    supergroup_id = None  # type: "int32"
    anyone_can_invite = None  # type: "Bool"


class toggleSupergroupSignMessages(Method):
    # Toggles sender signatures messages sent in a channel; requires appropriate
    # administrator rights in the channel. @supergroup_id Identifier of the channel
    # @sign_messages New value of sign_messages

    supergroup_id = None  # type: "int32"
    sign_messages = None  # type: "Bool"


class toggleSupergroupIsAllHistoryAvailable(Method):
    # Toggles whether the message history of a supergroup is available
    # to new members; requires appropriate administrator rights in the supergroup.
    # @supergroup_id The identifier of the supergroup @is_all_history_available The new value of is_all_history_available

    supergroup_id = None  # type: "int32"
    is_all_history_available = None  # type: "Bool"


class setSupergroupDescription(Method):
    # Changes information about a supergroup or channel; requires appropriate administrator
    # rights @supergroup_id Identifier of the supergroup or channel @param_description New
    # supergroup or channel description; 0-255 characters

    supergroup_id = None  # type: "int32"
    description = None  # type: "string"


class pinSupergroupMessage(Method):
    # Pins a message in a supergroup or channel; requires appropriate
    # administrator rights in the supergroup or channel @supergroup_id Identifier of
    # the supergroup or channel @message_id Identifier of the new pinned
    # message @disable_notification True, if there should be no notification about the pinned message

    supergroup_id = None  # type: "int32"
    message_id = None  # type: "int53"
    disable_notification = None  # type: "Bool"


class unpinSupergroupMessage(Method):
    # Removes the pinned message from a supergroup or channel; requires
    # appropriate administrator rights in the supergroup or channel @supergroup_id Identifier
    # of the supergroup or channel

    supergroup_id = None  # type: "int32"


class reportSupergroupSpam(Method):
    # Reports some messages from a user in a supergroup as
    # spam; requires administrator rights in the supergroup @supergroup_id Supergroup identifier
    # @user_id User identifier @message_ids Identifiers of messages sent in the
    # supergroup by the user. This list must be non-empty

    supergroup_id = None  # type: "int32"
    user_id = None  # type: "int32"
    message_ids = None  # type: "vector<int53>"


class deleteSupergroup(Method):
    # Deletes a supergroup or channel along with all messages in
    # the corresponding chat. This will release the supergroup or channel
    # username and remove all members; requires creator privileges in the
    # supergroup or channel. Chats with more than 1000 members can't
    # be deleted using this method @supergroup_id Identifier of the supergroup or channel

    supergroup_id = None  # type: "int32"


class closeSecretChat(Method):
    # Closes a secret chat, effectively transfering its state to secretChatStateClosed
    # @secret_chat_id Secret chat identifier

    secret_chat_id = None  # type: "int32"


class deleteSavedOrderInfo(Method):
    # Deletes saved order info

    pass


class deleteSavedCredentials(Method):
    # Deletes saved credentials for all payment provider bots

    pass


class setCustomLanguagePack(Method):
    # Adds or changes a custom language pack to the current
    # localization target @info Information about the language pack. Language pack
    # ID must start with 'X', consist only of English letters,
    # digits and hyphens, and must not exceed 64 characters @strings
    # Strings of the new language pack

    info = None  # type: "languagePackInfo"
    strings = None  # type: "vector<languagePackString>"


class editCustomLanguagePackInfo(Method):
    # Edits information about a custom language pack in the current
    # localization target @info New information about the custom language pack

    info = None  # type: "languagePackInfo"


class setCustomLanguagePackString(Method):
    # Adds, edits or deletes a string in a custom language
    # pack @language_pack_id Identifier of a previously added custom language pack
    # in the current localization target @new_string New language pack string

    language_pack_id = None  # type: "string"
    new_string = None  # type: "languagePackString"


class deleteLanguagePack(Method):
    # Deletes all information about a language pack in the current
    # localization target. The language pack that is currently in use
    # can't be deleted @language_pack_id Identifier of the language pack to delete

    language_pack_id = None  # type: "string"


class registerDevice(Method):
    # Registers the currently used device for receiving push notifications @device_token
    # Device token @other_user_ids List of at most 100 user identifiers
    # of other users currently using the client

    device_token = None  # type: "DeviceToken"
    other_user_ids = None  # type: "vector<int32>"


class setUserPrivacySettingRules(Method):
    # Changes user privacy settings @setting The privacy setting @rules The new privacy rules

    setting = None  # type: "UserPrivacySetting"
    rules = None  # type: "userPrivacySettingRules"


class setOption(Method):
    # Sets the value of an option. (Check the list of
    # available options on https://core.telegram.org/tdlib/options.) Only writable options can be set.
    # Can be called before authorization

    name = None  # type: "string"
    value = None  # type: "OptionValue"


class setAccountTtl(Method):
    # Changes the period of inactivity after which the account of
    # the current user will automatically be deleted @ttl New account TTL

    ttl = None  # type: "accountTtl"


class deleteAccount(Method):
    # Deletes the account of the current user, deleting all information
    # associated with the user from the server. The phone number
    # of the account can be used to create a new
    # account. Can be called before authorization when the current authorization
    # state is authorizationStateWaitPassword @reason The reason why the account was deleted; optional

    reason = None  # type: "string"


class changeChatReportSpamState(Method):
    # Used to let the server know whether a chat is
    # spam or not. Can be used only if ChatReportSpamState.can_report_spam is
    # true. After this request, ChatReportSpamState.can_report_spam becomes false forever @chat_id Chat
    # identifier @is_spam_chat If true, the chat will be reported as
    # spam; otherwise it will be marked as not spam

    chat_id = None  # type: "int53"
    is_spam_chat = None  # type: "Bool"


class reportChat(Method):
    # Reports a chat to the Telegram moderators. Supported only for
    # supergroups, channels, or private chats with bots, since other chats
    # can't be checked by moderators @chat_id Chat identifier @reason The
    # reason for reporting the chat @message_ids Identifiers of reported messages, if any

    chat_id = None  # type: "int53"
    reason = None  # type: "ChatReportReason"
    message_ids = None  # type: "vector<int53>"


class setNetworkType(Method):
    # Sets the current network type. Can be called before authorization.
    # Calling this method forces all network connections to reopen, mitigating
    # the delay in switching between different networks, so it should
    # be called whenever the network is changed, even if the
    # network type remains the same.

    type = None  # type: "NetworkType"


class addNetworkStatistics(Method):
    # Adds the specified data to data usage statistics. Can be
    # called before authorization @entry The network statistics entry with the
    # data to be added to statistics

    entry = None  # type: "NetworkStatisticsEntry"


class resetNetworkStatistics(Method):
    # Resets all network data usage statistics to zero. Can be called before authorization

    pass


class deletePassportElement(Method):
    # Deletes a Telegram Passport element @type Element type

    type = None  # type: "PassportElementType"


class setPassportElementErrors(Method):
    # Informs the user that some of the elements in their
    # Telegram Passport contain errors; for bots only. The user will
    # not be able to resend the elements, until the errors
    # are fixed @user_id User identifier @errors The errors

    user_id = None  # type: "int32"
    errors = None  # type: "vector<inputPassportElementError>"


class checkPhoneNumberVerificationCode(Method):
    # Checks the phone number verification code for Telegram Passport @code Verification code

    code = None  # type: "string"


class checkEmailAddressVerificationCode(Method):
    # Checks the email address verification code for Telegram Passport @code Verification code

    code = None  # type: "string"


class sendPassportAuthorizationForm(Method):
    # Sends a Telegram Passport authorization form, effectively sharing data with
    # the service @autorization_form_id Authorization form identifier @types Types of Telegram
    # Passport elements chosen by user to complete the authorization form

    autorization_form_id = None  # type: "int32"
    types = None  # type: "vector<PassportElementType>"


class checkPhoneNumberConfirmationCode(Method):
    # Checks phone number confirmation code @code The phone number confirmation code

    code = None  # type: "string"


class setBotUpdatesStatus(Method):
    # Informs the server about the number of pending bot updates
    # if they haven't been processed for a long time; for
    # bots only @pending_update_count The number of pending updates @error_message The last error message

    pending_update_count = None  # type: "int32"
    error_message = None  # type: "string"


class setStickerPositionInSet(Method):
    # Changes the position of a sticker in the set to
    # which it belongs; for bots only. The sticker set must
    # have been created by the bot @sticker Sticker @position New
    # position of the sticker in the set, zero-based

    sticker = None  # type: "InputFile"
    position = None  # type: "int32"


class removeStickerFromSet(Method):
    # Removes a sticker from the set to which it belongs;
    # for bots only. The sticker set must have been created
    # by the bot @sticker Sticker

    sticker = None  # type: "InputFile"


class acceptTermsOfService(Method):
    # Accepts Telegram terms of services @terms_of_service_id Terms of service identifier

    terms_of_service_id = None  # type: "string"


class answerCustomQuery(Method):
    # Answers a custom query; for bots only @custom_query_id Identifier of
    # a custom query @data JSON-serialized answer to the query

    custom_query_id = None  # type: "int64"
    data = None  # type: "string"


class setAlarm(Method):
    # Succeeds after a specified amount of time has passed. Can
    # be called before authorization. Can be called before initialization @seconds
    # Number of seconds before the function returns

    seconds = None  # type: "double"


class enableProxy(Method):
    # Enables a proxy. Only one proxy can be enabled at
    # a time. Can be called before authorization @proxy_id Proxy identifier

    proxy_id = None  # type: "int32"


class disableProxy(Method):
    # Disables the currently enabled proxy. Can be called before authorization

    pass


class removeProxy(Method):
    # Removes a proxy server. Can be called before authorization @proxy_id Proxy identifier

    proxy_id = None  # type: "int32"


class testCallEmpty(Method):
    # Does nothing; for testing only

    pass


class testNetwork(Method):
    # Sends a simple network request to the Telegram servers; for testing only

    pass


class testGetDifference(Method):
    # Forces an updates.getDifference call to the Telegram servers; for testing only

    pass
