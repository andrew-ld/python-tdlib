from ..factory import Method, Type


class webPageInstantView(Type):
    #  an instant view page for a web page @page_blocks
    #  of the web page @is_full True, if the instant
    #  contains the full page. A network request might be
    #  to get the full web page instant view

    page_blocks = None  # type: "vector<PageBlock>"
    is_full = None  # type: "Bool"


class getWebPageInstantView(Method):
    #  an instant view version of a web page if
    #  Returns a 404 error if the web page has
    #  instant view page @url The web page URL @force_full
    #  true, the full instant view for the web page will be returned

    url = None  # type: "string"
    force_full = None  # type: "Bool"
