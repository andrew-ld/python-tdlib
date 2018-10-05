from ..factory import Type


class inputInlineQueryResultAnimatedGif(Type):
    #  a link to an animated GIF @id Unique identifier
    #  the query result @title Title of the query result
    #  URL of the static result thumbnail (JPEG or GIF), if it exists

    id = None  # type: "string"
    title = None  # type: "string"
    thumbnail_url = None  # type: "string"
    gif_url = None  # type: "string"
    gif_duration = None  # type: "int32"
    gif_width = None  # type: "int32"
    gif_height = None  # type: "int32"
    reply_markup = None  # type: "ReplyMarkup"
    input_message_content = None  # type: "InputMessageContent"


class inputInlineQueryResultAnimatedMpeg4(Type):
    #  a link to an animated (i.e. without sound) H.264/MPEG-4
    #  video @id Unique identifier of the query result @title
    #  of the result @thumbnail_url URL of the static result
    #  (JPEG or GIF), if it exists

    id = None  # type: "string"
    title = None  # type: "string"
    thumbnail_url = None  # type: "string"
    mpeg4_url = None  # type: "string"
    mpeg4_duration = None  # type: "int32"
    mpeg4_width = None  # type: "int32"
    mpeg4_height = None  # type: "int32"
    reply_markup = None  # type: "ReplyMarkup"
    input_message_content = None  # type: "InputMessageContent"


class inputInlineQueryResultArticle(Type):
    #  a link to an article or web page @id
    #  identifier of the query result @url URL of the
    #  if it exists @hide_url True, if the URL must
    #  not shown @title Title of the result

    id = None  # type: "string"
    url = None  # type: "string"
    hide_url = None  # type: "Bool"
    title = None  # type: "string"
    description = None  # type: "string"
    thumbnail_url = None  # type: "string"
    thumbnail_width = None  # type: "int32"
    thumbnail_height = None  # type: "int32"
    reply_markup = None  # type: "ReplyMarkup"
    input_message_content = None  # type: "InputMessageContent"


class inputInlineQueryResultAudio(Type):
    #  a link to an MP3 audio file @id Unique
    #  of the query result @title Title of the audio
    #  @performer Performer of the audio file

    id = None  # type: "string"
    title = None  # type: "string"
    performer = None  # type: "string"
    audio_url = None  # type: "string"
    audio_duration = None  # type: "int32"
    reply_markup = None  # type: "ReplyMarkup"
    input_message_content = None  # type: "InputMessageContent"


class inputInlineQueryResultContact(Type):
    #  a user contact @id Unique identifier of the query
    #  @contact User contact @thumbnail_url URL of the result thumbnail,
    #  it exists @thumbnail_width Thumbnail width, if known @thumbnail_height Thumbnail height, if known

    id = None  # type: "string"
    contact = None  # type: "contact"
    thumbnail_url = None  # type: "string"
    thumbnail_width = None  # type: "int32"
    thumbnail_height = None  # type: "int32"
    reply_markup = None  # type: "ReplyMarkup"
    input_message_content = None  # type: "InputMessageContent"


class inputInlineQueryResultDocument(Type):
    #  a link to a file @id Unique identifier of
    #  query result @title Title of the resulting file @param_description
    #  description of the result, if known @document_url URL of
    #  file @mime_type MIME type of the file content; only
    #  and "application/zip" are currently allowed

    id = None  # type: "string"
    title = None  # type: "string"
    description = None  # type: "string"
    document_url = None  # type: "string"
    mime_type = None  # type: "string"
    thumbnail_url = None  # type: "string"
    thumbnail_width = None  # type: "int32"
    thumbnail_height = None  # type: "int32"
    reply_markup = None  # type: "ReplyMarkup"
    input_message_content = None  # type: "InputMessageContent"


class inputInlineQueryResultGame(Type):
    #  a game @id Unique identifier of the query result
    #  Short name of the game @reply_markup Message reply markup.
    #  be of type replyMarkupInlineKeyboard or null

    id = None  # type: "string"
    game_short_name = None  # type: "string"
    reply_markup = None  # type: "ReplyMarkup"


class inputInlineQueryResultLocation(Type):
    #  a point on the map @id Unique identifier of
    #  query result @location Location result @live_period Amount of time
    #  to the message sent time until the location can
    #  updated, in seconds @title Title of the result @thumbnail_url
    #  of the result thumbnail, if it exists @thumbnail_width Thumbnail
    #  if known @thumbnail_height Thumbnail height, if known

    id = None  # type: "string"
    location = None  # type: "location"
    live_period = None  # type: "int32"
    title = None  # type: "string"
    thumbnail_url = None  # type: "string"
    thumbnail_width = None  # type: "int32"
    thumbnail_height = None  # type: "int32"
    reply_markup = None  # type: "ReplyMarkup"
    input_message_content = None  # type: "InputMessageContent"


class inputInlineQueryResultPhoto(Type):
    #  link to a JPEG image @id Unique identifier of
    #  query result @title Title of the result, if known
    #  A short description of the result, if known @thumbnail_url
    #  of the photo thumbnail, if it exists

    id = None  # type: "string"
    title = None  # type: "string"
    description = None  # type: "string"
    thumbnail_url = None  # type: "string"
    photo_url = None  # type: "string"
    photo_width = None  # type: "int32"
    photo_height = None  # type: "int32"
    reply_markup = None  # type: "ReplyMarkup"
    input_message_content = None  # type: "InputMessageContent"


class inputInlineQueryResultSticker(Type):
    #  a link to a WEBP sticker @id Unique identifier
    #  the query result @thumbnail_url URL of the sticker thumbnail, if it exists

    id = None  # type: "string"
    thumbnail_url = None  # type: "string"
    sticker_url = None  # type: "string"
    sticker_width = None  # type: "int32"
    sticker_height = None  # type: "int32"
    reply_markup = None  # type: "ReplyMarkup"
    input_message_content = None  # type: "InputMessageContent"


class inputInlineQueryResultVenue(Type):
    #  information about a venue @id Unique identifier of the
    #  result @venue Venue result @thumbnail_url URL of the result
    #  if it exists @thumbnail_width Thumbnail width, if known @thumbnail_height
    #  height, if known

    id = None  # type: "string"
    venue = None  # type: "venue"
    thumbnail_url = None  # type: "string"
    thumbnail_width = None  # type: "int32"
    thumbnail_height = None  # type: "int32"
    reply_markup = None  # type: "ReplyMarkup"
    input_message_content = None  # type: "InputMessageContent"


class inputInlineQueryResultVideo(Type):
    #  a link to a page containing an embedded video
    #  or a video file @id Unique identifier of the
    #  result @title Title of the result @param_description A short
    #  of the result, if known

    id = None  # type: "string"
    title = None  # type: "string"
    description = None  # type: "string"
    thumbnail_url = None  # type: "string"
    video_url = None  # type: "string"
    mime_type = None  # type: "string"
    video_width = None  # type: "int32"
    video_height = None  # type: "int32"
    video_duration = None  # type: "int32"
    reply_markup = None  # type: "ReplyMarkup"
    input_message_content = None  # type: "InputMessageContent"


class inputInlineQueryResultVoiceNote(Type):
    #  a link to an opus-encoded audio file within an
    #  container, single channel audio @id Unique identifier of the
    #  result @title Title of the voice note

    id = None  # type: "string"
    title = None  # type: "string"
    voice_note_url = None  # type: "string"
    voice_note_duration = None  # type: "int32"
    reply_markup = None  # type: "ReplyMarkup"
    input_message_content = None  # type: "InputMessageContent"
