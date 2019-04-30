from ..factory import Type


class updateUnreadChatCount(Type):
	unread_count = None  # type: "int32"
	unread_unmuted_count = None  # type: "int32"
	marked_as_unread_count = None  # type: "int32"
	marked_as_unread_unmuted_count = None  # type: "int32"
