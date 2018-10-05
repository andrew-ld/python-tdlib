from ..factory import Type


class pageBlockTitle(Type):
    #  title of a page @title Title

    title = None  # type: "RichText"


class pageBlockSubtitle(Type):
    #  subtitle of a page @subtitle Subtitle

    subtitle = None  # type: "RichText"


class pageBlockAuthorDate(Type):
    #  author and publishing date of a page @author Author
    #  Point in time (Unix timestamp) when the article was
    #  0 if unknown

    author = None  # type: "RichText"
    publish_date = None  # type: "int32"


class pageBlockHeader(Type):
    #  header @header Header

    header = None  # type: "RichText"


class pageBlockSubheader(Type):
    #  subheader @subheader Subheader

    subheader = None  # type: "RichText"


class pageBlockParagraph(Type):
    #  text paragraph @text Paragraph text

    text = None  # type: "RichText"


class pageBlockPreformatted(Type):
    #  preformatted text paragraph @text Paragraph text @language Programming language
    #  which the text should be formatted

    text = None  # type: "RichText"
    language = None  # type: "string"


class pageBlockFooter(Type):
    #  footer of a page @footer Footer

    footer = None  # type: "RichText"


class pageBlockDivider(Type):
    #  empty block separating a page

    pass


class pageBlockAnchor(Type):
    #  invisible anchor on a page, which can be used
    #  a URL to open the page from the specified
    #  @name Name of the anchor

    name = None  # type: "string"


class pageBlockList(Type):
    #  list of texts @items Texts @is_ordered True, if the
    #  should be marked with numbers

    items = None  # type: "vector<RichText>"
    is_ordered = None  # type: "Bool"


class pageBlockBlockQuote(Type):
    #  block quote @text Quote text @caption Quote caption

    text = None  # type: "RichText"
    caption = None  # type: "RichText"


class pageBlockPullQuote(Type):
    #  pull quote @text Quote text @caption Quote caption

    text = None  # type: "RichText"
    caption = None  # type: "RichText"


class pageBlockAnimation(Type):
    #  animation @animation Animation file; may be null @caption Animation
    #  @need_autoplay True, if the animation should be played automatically

    animation = None  # type: "animation"
    caption = None  # type: "RichText"
    need_autoplay = None  # type: "Bool"


class pageBlockAudio(Type):
    #  audio file @audio Audio file; may be null @caption Audio file caption

    audio = None  # type: "audio"
    caption = None  # type: "RichText"


class pageBlockPhoto(Type):
    #  photo @photo Photo file; may be null @caption Photo

    photo = None  # type: "photo"
    caption = None  # type: "RichText"


class pageBlockVideo(Type):
    #  video @video Video file; may be null @caption Video
    #  @need_autoplay True, if the video should be played automatically
    #  True, if the video should be looped

    video = None  # type: "video"
    caption = None  # type: "RichText"
    need_autoplay = None  # type: "Bool"
    is_looped = None  # type: "Bool"


class pageBlockCover(Type):
    #  page cover @cover Cover

    cover = None  # type: "PageBlock"


class pageBlockEmbedded(Type):
    #  embedded web page @url Web page URL, if available
    #  HTML-markup of the embedded page @poster_photo Poster photo, if
    #  may be null @width Block width @height Block height
    #  Block caption @is_full_width True, if the block should be
    #  width @allow_scrolling True, if scrolling should be allowed

    url = None  # type: "string"
    html = None  # type: "string"
    poster_photo = None  # type: "photo"
    width = None  # type: "int32"
    height = None  # type: "int32"
    caption = None  # type: "RichText"
    is_full_width = None  # type: "Bool"
    allow_scrolling = None  # type: "Bool"


class pageBlockEmbeddedPost(Type):
    #  embedded post @url Web page URL @author Post author
    #  Post author photo @date Point in time (Unix timestamp)
    #  the post was created; 0 if unknown @page_blocks Post
    #  @caption Post caption

    url = None  # type: "string"
    author = None  # type: "string"
    author_photo = None  # type: "photo"
    date = None  # type: "int32"
    page_blocks = None  # type: "vector<PageBlock>"
    caption = None  # type: "RichText"


class pageBlockCollage(Type):
    #  collage @page_blocks Collage item contents @caption Block caption

    page_blocks = None  # type: "vector<PageBlock>"
    caption = None  # type: "RichText"


class pageBlockSlideshow(Type):
    #  slideshow @page_blocks Slideshow item contents @caption Block caption

    page_blocks = None  # type: "vector<PageBlock>"
    caption = None  # type: "RichText"


class pageBlockChatLink(Type):
    #  link to a chat @title Chat title @photo Chat
    #  may be null @username Chat username, by which all
    #  information about the chat should be resolved

    title = None  # type: "string"
    photo = None  # type: "chatPhoto"
    username = None  # type: "string"
