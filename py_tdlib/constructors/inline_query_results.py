from ..factory import Method, Type


class inlineQueryResults(Type):
    #  the results of the inline query. Use sendInlineQueryResultMessage to
    #  the result of the query @inline_query_id Unique identifier of
    #  inline query @next_offset The offset for the next request.
    #  empty, there are no more results @results Results of the query

    inline_query_id = None  # type: "int64"
    next_offset = None  # type: "string"
    results = None  # type: "vector<InlineQueryResult>"
    switch_pm_text = None  # type: "string"
    switch_pm_parameter = None  # type: "string"


class getInlineQueryResults(Method):
    #  an inline query to a bot and returns its
    #  Returns an error with code 502 if the bot
    #  to answer the query before the query timeout expires
    #  The identifier of the target bot

    bot_user_id = None  # type: "int32"
    chat_id = None  # type: "int53"
    user_location = None  # type: "location"
    query = None  # type: "string"
    offset = None  # type: "string"
