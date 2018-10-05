from ..factory import Type


class userTypeRegular(Type):
    #  regular user

    pass


class userTypeDeleted(Type):
    #  deleted user or deleted bot. No information on the
    #  besides the user_id is available. It is not possible
    #  perform any active actions on this type of user

    pass


class userTypeBot(Type):
    #  bot (see https://core.telegram.org/bots) @can_join_groups True, if the bot can
    #  invited to basic group and supergroup chats

    can_join_groups = None  # type: "Bool"
    can_read_all_group_messages = None  # type: "Bool"
    is_inline = None  # type: "Bool"
    inline_query_placeholder = None  # type: "string"
    need_location = None  # type: "Bool"


class userTypeUnknown(Type):
    #  information on the user besides the user_id is available,
    #  this user has not been deleted. This object is
    #  rare and must be handled like a deleted user.
    #  is not possible to perform any actions on users of this type

    pass
