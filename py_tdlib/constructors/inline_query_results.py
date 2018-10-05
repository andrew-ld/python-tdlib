from ..factory import Method, Type


class inlineQueryResults(Type):
    # Represents the results of the inline query. Use sendInlineQueryResultMessage to
    # send the result of the query @inline_query_id Unique identifier of
    # the inline query @next_offset The offset for the next request.
    # If empty, there are no more results @results Results of the query

    inline_query_id = None  # type: "int64"
    next_offset = None  # type: "string"
    results = None  # type: "vector<InlineQueryResult>"
    switch_pm_text = None  # type: "string"
    switch_pm_parameter = None  # type: "string"


class getInlineQueryResults(Method):
    # Sends an inline query to a bot and returns its
    # results. Returns an error with code 502 if the bot
    # fails to answer the query before the query timeout expires
    # @bot_user_id The identifier of the target bot

    bot_user_id = None  # type: "int32"
    chat_id = None  # type: "int53"
    user_location = None  # type: "location"
    query = None  # type: "string"
    offset = None  # type: "string"
