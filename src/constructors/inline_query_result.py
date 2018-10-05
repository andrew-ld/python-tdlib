from tdwrapper.factory import Type


class inlineQueryResultArticle(Type):
    #  a link to an article or web page @id
    #  identifier of the query result @url URL of the
    #  if it exists @hide_url True, if the URL must
    #  not shown @title Title of the result

    id = None  # type: "string"
    url = None  # type: "string"
    hide_url = None  # type: "Bool"
    title = None  # type: "string"
    description = None  # type: "string"
    thumbnail = None  # type: "photoSize"


class inlineQueryResultContact(Type):
    #  a user contact @id Unique identifier of the query
    #  @contact A user contact @thumbnail Result thumbnail; may be

    id = None  # type: "string"
    contact = None  # type: "contact"
    thumbnail = None  # type: "photoSize"


class inlineQueryResultLocation(Type):
    #  a point on the map @id Unique identifier of
    #  query result @location Location result @title Title of the
    #  @thumbnail Result thumbnail; may be null

    id = None  # type: "string"
    location = None  # type: "location"
    title = None  # type: "string"
    thumbnail = None  # type: "photoSize"


class inlineQueryResultVenue(Type):
    #  information about a venue @id Unique identifier of the
    #  result @venue Venue result @thumbnail Result thumbnail; may be

    id = None  # type: "string"
    venue = None  # type: "venue"
    thumbnail = None  # type: "photoSize"


class inlineQueryResultGame(Type):
    #  information about a game @id Unique identifier of the
    #  result @game Game result

    id = None  # type: "string"
    game = None  # type: "game"


class inlineQueryResultAnimation(Type):
    #  an animation file @id Unique identifier of the query
    #  @animation Animation file @title Animation title

    id = None  # type: "string"
    animation = None  # type: "animation"
    title = None  # type: "string"


class inlineQueryResultAudio(Type):
    #  an audio file @id Unique identifier of the query
    #  @audio Audio file

    id = None  # type: "string"
    audio = None  # type: "audio"


class inlineQueryResultDocument(Type):
    #  a document @id Unique identifier of the query result
    #  Document @title Document title @param_description Document description

    id = None  # type: "string"
    document = None  # type: "document"
    title = None  # type: "string"
    description = None  # type: "string"


class inlineQueryResultPhoto(Type):
    #  a photo @id Unique identifier of the query result
    #  Photo @title Title of the result, if known @param_description
    #  short description of the result, if known

    id = None  # type: "string"
    photo = None  # type: "photo"
    title = None  # type: "string"
    description = None  # type: "string"


class inlineQueryResultSticker(Type):
    #  a sticker @id Unique identifier of the query result @sticker Sticker

    id = None  # type: "string"
    sticker = None  # type: "sticker"


class inlineQueryResultVideo(Type):
    #  a video @id Unique identifier of the query result
    #  Video @title Title of the video @param_description Description of the video

    id = None  # type: "string"
    video = None  # type: "video"
    title = None  # type: "string"
    description = None  # type: "string"


class inlineQueryResultVoiceNote(Type):
    #  a voice note @id Unique identifier of the query
    #  @voice_note Voice note @title Title of the voice note

    id = None  # type: "string"
    voice_note = None  # type: "voiceNote"
    title = None  # type: "string"
