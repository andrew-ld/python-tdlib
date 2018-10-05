from ..factory import Type


class messageText(Type):
    # A text message @text Text of the message @web_page A
    # preview of the web page that's mentioned in the text; may be null

    text = None  # type: "formattedText"
    web_page = None  # type: "webPage"


class messageAnimation(Type):
    # An animation message (GIF-style). @animation Message content @caption Animation caption
    # @is_secret True, if the animation thumbnail must be blurred and
    # the animation must be shown only while tapped

    animation = None  # type: "animation"
    caption = None  # type: "formattedText"
    is_secret = None  # type: "Bool"


class messageAudio(Type):
    # An audio message @audio Message content @caption Audio caption

    audio = None  # type: "audio"
    caption = None  # type: "formattedText"


class messageDocument(Type):
    # A document message (general file) @document Message content @caption Document caption

    document = None  # type: "document"
    caption = None  # type: "formattedText"


class messagePhoto(Type):
    # A photo message @photo Message content @caption Photo caption @is_secret
    # True, if the photo must be blurred and must be
    # shown only while tapped

    photo = None  # type: "photo"
    caption = None  # type: "formattedText"
    is_secret = None  # type: "Bool"


class messageExpiredPhoto(Type):
    # An expired photo message (self-destructed after TTL has elapsed)

    pass


class messageSticker(Type):
    # A sticker message @sticker Message content

    sticker = None  # type: "sticker"


class messageVideo(Type):
    # A video message @video Message content @caption Video caption @is_secret
    # True, if the video thumbnail must be blurred and the
    # video must be shown only while tapped

    video = None  # type: "video"
    caption = None  # type: "formattedText"
    is_secret = None  # type: "Bool"


class messageExpiredVideo(Type):
    # An expired video message (self-destructed after TTL has elapsed)

    pass


class messageVideoNote(Type):
    # A video note message @video_note Message content @is_viewed True, if
    # at least one of the recipients has viewed the video
    # note @is_secret True, if the video note thumbnail must be
    # blurred and the video note must be shown only while tapped

    video_note = None  # type: "videoNote"
    is_viewed = None  # type: "Bool"
    is_secret = None  # type: "Bool"


class messageVoiceNote(Type):
    # A voice note message @voice_note Message content @caption Voice note
    # caption @is_listened True, if at least one of the recipients
    # has listened to the voice note

    voice_note = None  # type: "voiceNote"
    caption = None  # type: "formattedText"
    is_listened = None  # type: "Bool"


class messageLocation(Type):
    # A message with a location @location Message content @live_period Time
    # relative to the message sent date until which the location
    # can be updated, in seconds

    location = None  # type: "location"
    live_period = None  # type: "int32"
    expires_in = None  # type: "int32"


class messageVenue(Type):
    # A message with information about a venue @venue Message content

    venue = None  # type: "venue"


class messageContact(Type):
    # A message with a user contact @contact Message content

    contact = None  # type: "contact"


class messageGame(Type):
    # A message with a game @game Game

    game = None  # type: "game"


class messageInvoice(Type):
    # A message with an invoice from a bot @title Product
    # title @param_description Product description @photo Product photo; may be null
    # @currency Currency for the product price @total_amount Product total price
    # in the minimal quantity of the currency

    title = None  # type: "string"
    description = None  # type: "string"
    photo = None  # type: "photo"
    currency = None  # type: "string"
    total_amount = None  # type: "int53"
    start_parameter = None  # type: "string"
    is_test = None  # type: "Bool"
    need_shipping_address = None  # type: "Bool"
    receipt_message_id = None  # type: "int53"


class messageCall(Type):
    # A message with information about an ended call @discard_reason Reason
    # why the call was discarded @duration Call duration, in seconds

    discard_reason = None  # type: "CallDiscardReason"
    duration = None  # type: "int32"


class messageBasicGroupChatCreate(Type):
    # A newly created basic group @title Title of the basic
    # group @member_user_ids User identifiers of members in the basic group

    title = None  # type: "string"
    member_user_ids = None  # type: "vector<int32>"


class messageSupergroupChatCreate(Type):
    # A newly created supergroup or channel @title Title of the supergroup or channel

    title = None  # type: "string"


class messageChatChangeTitle(Type):
    # An updated chat title @title New chat title

    title = None  # type: "string"


class messageChatChangePhoto(Type):
    # An updated chat photo @photo New chat photo

    photo = None  # type: "photo"


class messageChatDeletePhoto(Type):
    # A deleted chat photo

    pass


class messageChatAddMembers(Type):
    # New chat members were added @member_user_ids User identifiers of the new members

    member_user_ids = None  # type: "vector<int32>"


class messageChatJoinByLink(Type):
    # A new member joined the chat by invite link

    pass


class messageChatDeleteMember(Type):
    # A chat member was deleted @user_id User identifier of the deleted chat member

    user_id = None  # type: "int32"


class messageChatUpgradeTo(Type):
    # A basic group was upgraded to a supergroup and was
    # deactivated as the result @supergroup_id Identifier of the supergroup to
    # which the basic group was upgraded

    supergroup_id = None  # type: "int32"


class messageChatUpgradeFrom(Type):
    # A supergroup has been created from a basic group @title
    # Title of the newly created supergroup @basic_group_id The identifier of
    # the original basic group

    title = None  # type: "string"
    basic_group_id = None  # type: "int32"


class messagePinMessage(Type):
    # A message has been pinned @message_id Identifier of the pinned
    # message, can be an identifier of a deleted message

    message_id = None  # type: "int53"


class messageScreenshotTaken(Type):
    # A screenshot of a message in the chat has been taken

    pass


class messageChatSetTtl(Type):
    # The TTL (Time To Live) setting messages in a secret
    # chat has been changed @ttl New TTL

    ttl = None  # type: "int32"


class messageCustomServiceAction(Type):
    # A non-standard action has happened in the chat @text Message
    # text to be shown in the chat

    text = None  # type: "string"


class messageGameScore(Type):
    # A new high score was achieved in a game @game_message_id
    # Identifier of the message with the game, can be an
    # identifier of a deleted message @game_id Identifier of the game,
    # may be different from the games presented in the message
    # with the game @score New score

    game_message_id = None  # type: "int53"
    game_id = None  # type: "int64"
    score = None  # type: "int32"


class messagePaymentSuccessful(Type):
    # A payment has been completed @invoice_message_id Identifier of the message
    # with the corresponding invoice; can be an identifier of a
    # deleted message @currency Currency for the price of the product
    # @total_amount Total price for the product, in the minimal quantity of the currency

    invoice_message_id = None  # type: "int53"
    currency = None  # type: "string"
    total_amount = None  # type: "int53"


class messagePaymentSuccessfulBot(Type):
    # A payment has been completed; for bots only @invoice_message_id Identifier
    # of the message with the corresponding invoice; can be an
    # identifier of a deleted message @currency Currency for price of the product

    invoice_message_id = None  # type: "int53"
    currency = None  # type: "string"
    total_amount = None  # type: "int53"
    invoice_payload = None  # type: "bytes"
    shipping_option_id = None  # type: "string"
    order_info = None  # type: "orderInfo"
    telegram_payment_charge_id = None  # type: "string"
    provider_payment_charge_id = None  # type: "string"


class messageContactRegistered(Type):
    # A contact has registered with Telegram

    pass


class messageWebsiteConnected(Type):
    # The current user has connected a website by logging in
    # using Telegram Login Widget on it @domain_name Domain name of the connected website

    domain_name = None  # type: "string"


class messagePassportDataSent(Type):
    # Telegram Passport data has been sent @types List of Telegram
    # Passport element types sent

    types = None  # type: "vector<PassportElementType>"


class messagePassportDataReceived(Type):
    # Telegram Passport data has been received; for bots only @elements
    # List of received Telegram Passport elements @credentials Encrypted data credentials

    elements = None  # type: "vector<encryptedPassportElement>"
    credentials = None  # type: "encryptedCredentials"


class messageUnsupported(Type):
    # Message content that is not supported by the client

    pass
