from ..factory import Method, Type


class webPage(Type):
    # Describes a web page preview, @url Original URL of the
    # link, @display_url URL to display

    url = None  # type: "string"
    display_url = None  # type: "string"
    type = None  # type: "string"
    site_name = None  # type: "string"
    title = None  # type: "string"
    description = None  # type: "string"
    photo = None  # type: "photo"
    embed_url = None  # type: "string"
    embed_type = None  # type: "string"
    embed_width = None  # type: "int32"
    embed_height = None  # type: "int32"
    duration = None  # type: "int32"
    author = None  # type: "string"
    animation = None  # type: "animation"
    audio = None  # type: "audio"
    document = None  # type: "document"
    sticker = None  # type: "sticker"
    video = None  # type: "video"
    video_note = None  # type: "videoNote"
    voice_note = None  # type: "voiceNote"
    has_instant_view = None  # type: "Bool"


class getWebPagePreview(Method):
    # Returns a web page preview by the text of the
    # message. Do not call this function too often. Returns a
    # 404 error if the web page has no preview, @text
    # Message text with formatting

    text = None  # type: "formattedText"
