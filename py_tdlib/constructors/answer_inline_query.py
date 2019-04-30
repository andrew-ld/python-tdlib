from ..factory import Method


class answerInlineQuery(Method):
	inline_query_id = None  # type: "int64"
	is_personal = None  # type: "Bool"
	results = None  # type: "vector<InputInlineQueryResult>"
	cache_time = None  # type: "int32"
	next_offset = None  # type: "string"
	switch_pm_text = None  # type: "string"
	switch_pm_parameter = None  # type: "string"
