from ..factory import Type


class messageText(Type):
    #  text message @text Text of the message @web_page A
    #  of the web page that's mentioned in the text; may be null

    text = None  # type: "formattedText"
    web_page = None  # type: "webPage"


class messageAnimation(Type):
    #  animation message (GIF-style). @animation Message content @caption Animation caption
    #  True, if the animation thumbnail must be blurred and
    #  animation must be shown only while tapped

    animation = None  # type: "animation"
    caption = None  # type: "formattedText"
    is_secret = None  # type: "Bool"


class messageAudio(Type):
    #  audio message @audio Message content @caption Audio caption

    audio = None  # type: "audio"
    caption = None  # type: "formattedText"


class messageDocument(Type):
    #  document message (general file) @document Message content @caption Document

    document = None  # type: "document"
    caption = None  # type: "formattedText"


class messagePhoto(Type):
    #  photo message @photo Message content @caption Photo caption @is_secret
    #  if the photo must be blurred and must be
    #  only while tapped

    photo = None  # type: "photo"
    caption = None  # type: "formattedText"
    is_secret = None  # type: "Bool"


class messageExpiredPhoto(Type):
    #  expired photo message (self-destructed after TTL has elapsed)

    pass


class messageSticker(Type):
    #  sticker message @sticker Message content

    sticker = None  # type: "sticker"


class messageVideo(Type):
    #  video message @video Message content @caption Video caption @is_secret
    #  if the video thumbnail must be blurred and the
    #  must be shown only while tapped

    video = None  # type: "video"
    caption = None  # type: "formattedText"
    is_secret = None  # type: "Bool"


class messageExpiredVideo(Type):
    #  expired video message (self-destructed after TTL has elapsed)

    pass


class messageVideoNote(Type):
    #  video note message @video_note Message content @is_viewed True, if
    #  least one of the recipients has viewed the video
    #  @is_secret True, if the video note thumbnail must be
    #  and the video note must be shown only while

    video_note = None  # type: "videoNote"
    is_viewed = None  # type: "Bool"
    is_secret = None  # type: "Bool"


class messageVoiceNote(Type):
    #  voice note message @voice_note Message content @caption Voice note
    #  @is_listened True, if at least one of the recipients
    #  listened to the voice note

    voice_note = None  # type: "voiceNote"
    caption = None  # type: "formattedText"
    is_listened = None  # type: "Bool"


class messageLocation(Type):
    #  message with a location @location Message content @live_period Time
    #  to the message sent date until which the location
    #  be updated, in seconds

    location = None  # type: "location"
    live_period = None  # type: "int32"
    expires_in = None  # type: "int32"


class messageVenue(Type):
    #  message with information about a venue @venue Message content

    venue = None  # type: "venue"


class messageContact(Type):
    #  message with a user contact @contact Message content

    contact = None  # type: "contact"


class messageGame(Type):
    #  message with a game @game Game

    game = None  # type: "game"


class messageInvoice(Type):
    #  message with an invoice from a bot @title Product
    #  @param_description Product description @photo Product photo; may be null
    #  Currency for the product price @total_amount Product total price
    #  the minimal quantity of the currency

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
    #  message with information about an ended call @discard_reason Reason
    #  the call was discarded @duration Call duration, in seconds

    discard_reason = None  # type: "CallDiscardReason"
    duration = None  # type: "int32"


class messageBasicGroupChatCreate(Type):
    #  newly created basic group @title Title of the basic
    #  @member_user_ids User identifiers of members in the basic group

    title = None  # type: "string"
    member_user_ids = None  # type: "vector<int32>"


class messageSupergroupChatCreate(Type):
    #  newly created supergroup or channel @title Title of the supergroup or channel

    title = None  # type: "string"


class messageChatChangeTitle(Type):
    #  updated chat title @title New chat title

    title = None  # type: "string"


class messageChatChangePhoto(Type):
    #  updated chat photo @photo New chat photo

    photo = None  # type: "photo"


class messageChatDeletePhoto(Type):
    #  deleted chat photo

    pass


class messageChatAddMembers(Type):
    #  chat members were added @member_user_ids User identifiers of the new members

    member_user_ids = None  # type: "vector<int32>"


class messageChatJoinByLink(Type):
    #  new member joined the chat by invite link

    pass


class messageChatDeleteMember(Type):
    #  chat member was deleted @user_id User identifier of the deleted chat member

    user_id = None  # type: "int32"


class messageChatUpgradeTo(Type):
    #  basic group was upgraded to a supergroup and was
    #  as the result @supergroup_id Identifier of the supergroup to
    #  the basic group was upgraded

    supergroup_id = None  # type: "int32"


class messageChatUpgradeFrom(Type):
    #  supergroup has been created from a basic group @title
    #  of the newly created supergroup @basic_group_id The identifier of
    #  original basic group

    title = None  # type: "string"
    basic_group_id = None  # type: "int32"


class messagePinMessage(Type):
    #  message has been pinned @message_id Identifier of the pinned
    #  can be an identifier of a deleted message

    message_id = None  # type: "int53"


class messageScreenshotTaken(Type):
    #  screenshot of a message in the chat has been

    pass


class messageChatSetTtl(Type):
    #  TTL (Time To Live) setting messages in a secret
    #  has been changed @ttl New TTL

    ttl = None  # type: "int32"


class messageCustomServiceAction(Type):
    #  non-standard action has happened in the chat @text Message
    #  to be shown in the chat

    text = None  # type: "string"


class messageGameScore(Type):
    #  new high score was achieved in a game @game_message_id
    #  of the message with the game, can be an
    #  of a deleted message @game_id Identifier of the game,
    #  be different from the games presented in the message
    #  the game @score New score

    game_message_id = None  # type: "int53"
    game_id = None  # type: "int64"
    score = None  # type: "int32"


class messagePaymentSuccessful(Type):
    #  payment has been completed @invoice_message_id Identifier of the message
    #  the corresponding invoice; can be an identifier of a
    #  message @currency Currency for the price of the product
    #  Total price for the product, in the minimal quantity of the currency

    invoice_message_id = None  # type: "int53"
    currency = None  # type: "string"
    total_amount = None  # type: "int53"


class messagePaymentSuccessfulBot(Type):
    #  payment has been completed; for bots only @invoice_message_id Identifier
    #  the message with the corresponding invoice; can be an
    #  of a deleted message @currency Currency for price of the product

    invoice_message_id = None  # type: "int53"
    currency = None  # type: "string"
    total_amount = None  # type: "int53"
    invoice_payload = None  # type: "bytes"
    shipping_option_id = None  # type: "string"
    order_info = None  # type: "orderInfo"
    telegram_payment_charge_id = None  # type: "string"
    provider_payment_charge_id = None  # type: "string"


class messageContactRegistered(Type):
    #  contact has registered with Telegram

    pass


class messageWebsiteConnected(Type):
    #  current user has connected a website by logging in
    #  Telegram Login Widget on it @domain_name Domain name of the connected website

    domain_name = None  # type: "string"


class messagePassportDataSent(Type):
    #  Passport data has been sent @types List of Telegram
    #  element types sent

    types = None  # type: "vector<PassportElementType>"


class messagePassportDataReceived(Type):
    #  Passport data has been received; for bots only @elements
    #  of received Telegram Passport elements @credentials Encrypted data credentials

    elements = None  # type: "vector<encryptedPassportElement>"
    credentials = None  # type: "encryptedCredentials"


class messageUnsupported(Type):
    #  content that is not supported by the client

    pass
