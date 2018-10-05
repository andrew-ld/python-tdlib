from ..factory import Type


class pageBlockTitle(Type):
    # The title of a page, @title Title

    title = None  # type: "RichText"


class pageBlockSubtitle(Type):
    # The subtitle of a page, @subtitle Subtitle

    subtitle = None  # type: "RichText"


class pageBlockAuthorDate(Type):
    # The author and publishing date of a page, @author Author
    # @publish_date Point in time (Unix timestamp) when the article was
    # published; 0 if unknown

    author = None  # type: "RichText"
    publish_date = None  # type: "int32"


class pageBlockHeader(Type):
    # A header, @header Header

    header = None  # type: "RichText"


class pageBlockSubheader(Type):
    # A subheader, @subheader Subheader

    subheader = None  # type: "RichText"


class pageBlockParagraph(Type):
    # A text paragraph, @text Paragraph text

    text = None  # type: "RichText"


class pageBlockPreformatted(Type):
    # A preformatted text paragraph, @text Paragraph text, @language Programming language
    # for which the text should be formatted

    text = None  # type: "RichText"
    language = None  # type: "string"


class pageBlockFooter(Type):
    # The footer of a page, @footer Footer

    footer = None  # type: "RichText"


class pageBlockDivider(Type):
    # An empty block separating a page

    pass


class pageBlockAnchor(Type):
    # An invisible anchor on a page, which can be used
    # in a URL to open the page from the specified
    # anchor, @name Name of the anchor

    name = None  # type: "string"


class pageBlockList(Type):
    # A list of texts, @items Texts, @is_ordered True, if the
    # items should be marked with numbers

    items = None  # type: "vector<RichText>"
    is_ordered = None  # type: "Bool"


class pageBlockBlockQuote(Type):
    # A block quote, @text Quote text, @caption Quote caption

    text = None  # type: "RichText"
    caption = None  # type: "RichText"


class pageBlockPullQuote(Type):
    # A pull quote, @text Quote text, @caption Quote caption

    text = None  # type: "RichText"
    caption = None  # type: "RichText"


class pageBlockAnimation(Type):
    # An animation, @animation Animation file; may be null, @caption Animation
    # caption, @need_autoplay True, if the animation should be played automatically

    animation = None  # type: "animation"
    caption = None  # type: "RichText"
    need_autoplay = None  # type: "Bool"


class pageBlockAudio(Type):
    # An audio file, @audio Audio file; may be null, @caption Audio file caption

    audio = None  # type: "audio"
    caption = None  # type: "RichText"


class pageBlockPhoto(Type):
    # A photo, @photo Photo file; may be null, @caption Photo caption

    photo = None  # type: "photo"
    caption = None  # type: "RichText"


class pageBlockVideo(Type):
    # A video, @video Video file; may be null, @caption Video
    # caption, @need_autoplay True, if the video should be played automatically
    # @is_looped True, if the video should be looped

    video = None  # type: "video"
    caption = None  # type: "RichText"
    need_autoplay = None  # type: "Bool"
    is_looped = None  # type: "Bool"


class pageBlockCover(Type):
    # A page cover, @cover Cover

    cover = None  # type: "PageBlock"


class pageBlockEmbedded(Type):
    # An embedded web page, @url Web page URL, if available
    # @html HTML-markup of the embedded page, @poster_photo Poster photo, if
    # available; may be null, @width Block width, @height Block height
    # @caption Block caption, @is_full_width True, if the block should be
    # full width, @allow_scrolling True, if scrolling should be allowed

    url = None  # type: "string"
    html = None  # type: "string"
    poster_photo = None  # type: "photo"
    width = None  # type: "int32"
    height = None  # type: "int32"
    caption = None  # type: "RichText"
    is_full_width = None  # type: "Bool"
    allow_scrolling = None  # type: "Bool"


class pageBlockEmbeddedPost(Type):
    # An embedded post, @url Web page URL, @author Post author
    # @author_photo Post author photo, @date Point in time (Unix timestamp)
    # when the post was created; 0 if unknown, @page_blocks Post
    # content, @caption Post caption

    url = None  # type: "string"
    author = None  # type: "string"
    author_photo = None  # type: "photo"
    date = None  # type: "int32"
    page_blocks = None  # type: "vector<PageBlock>"
    caption = None  # type: "RichText"


class pageBlockCollage(Type):
    # A collage, @page_blocks Collage item contents, @caption Block caption

    page_blocks = None  # type: "vector<PageBlock>"
    caption = None  # type: "RichText"


class pageBlockSlideshow(Type):
    # A slideshow, @page_blocks Slideshow item contents, @caption Block caption

    page_blocks = None  # type: "vector<PageBlock>"
    caption = None  # type: "RichText"


class pageBlockChatLink(Type):
    # A link to a chat, @title Chat title, @photo Chat
    # photo; may be null, @username Chat username, by which all
    # other information about the chat should be resolved

    title = None  # type: "string"
    photo = None  # type: "chatPhoto"
    username = None  # type: "string"
