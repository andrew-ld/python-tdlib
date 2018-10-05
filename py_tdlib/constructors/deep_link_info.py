from ..factory import Method, Type


class deepLinkInfo(Type):
    # Contains information about a tg:// deep link, @text Text to
    # be shown to the user, @need_update_application True, if user should
    # be asked to update the application

    text = None  # type: "formattedText"
    need_update_application = None  # type: "Bool"


class getDeepLinkInfo(Method):
    # Returns information about a tg:// deep link. Use "tg://need_update_for_some_feature" or
    # "tg:some_unsupported_feature" for testing. Returns a 404 error for unknown links.
    # Can be called before authorization, @link The link

    link = None  # type: "string"
