from ..factory import Type


class tMeUrlTypeUser(Type):
    # A URL linking to a user, @user_id Identifier of the user

    user_id = None  # type: "int32"


class tMeUrlTypeSupergroup(Type):
    # A URL linking to a public supergroup or channel, @supergroup_id
    # Identifier of the supergroup or channel

    supergroup_id = None  # type: "int53"


class tMeUrlTypeChatInvite(Type):
    # A chat invite link, @info Chat invite link info

    info = None  # type: "chatInviteLinkInfo"


class tMeUrlTypeStickerSet(Type):
    # A URL linking to a sticker set, @sticker_set_id Identifier of the sticker set

    sticker_set_id = None  # type: "int64"
