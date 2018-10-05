from ..factory import Method, Type


class deepLinkInfo(Type):
    #  information about a tg:// deep link @text Text to
    #  shown to the user @need_update_application True, if user should
    #  asked to update the application

    text = None  # type: "formattedText"
    need_update_application = None  # type: "Bool"


class getDeepLinkInfo(Method):
    #  information about a tg:// deep link. Use "tg://need_update_for_some_feature" or
    #  for testing. Returns a 404 error for unknown links.
    #  be called before authorization @link The link

    link = None  # type: "string"
