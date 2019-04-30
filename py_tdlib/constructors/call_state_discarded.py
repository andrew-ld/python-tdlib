from ..factory import Type


class callStateDiscarded(Type):
	reason = None  # type: "CallDiscardReason"
	need_rating = None  # type: "Bool"
	need_debug_information = None  # type: "Bool"
