from ..factory import Type


class inlineQueryResults(Type):
	inline_query_id = None  # type: "int64"
	next_offset = None  # type: "string"
	results = None  # type: "vector<InlineQueryResult>"
	switch_pm_text = None  # type: "string"
	switch_pm_parameter = None  # type: "string"
