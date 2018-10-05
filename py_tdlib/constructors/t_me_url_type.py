from ..factory import Type


class tMeUrlTypeUser(Type):
    #  URL linking to a user @user_id Identifier of the

    user_id = None  # type: "int32"


class tMeUrlTypeSupergroup(Type):
    #  URL linking to a public supergroup or channel @supergroup_id
    #  of the supergroup or channel

    supergroup_id = None  # type: "int53"


class tMeUrlTypeChatInvite(Type):
    #  chat invite link @info Chat invite link info

    info = None  # type: "chatInviteLinkInfo"


class tMeUrlTypeStickerSet(Type):
    #  URL linking to a sticker set @sticker_set_id Identifier of the sticker set

    sticker_set_id = None  # type: "int64"
