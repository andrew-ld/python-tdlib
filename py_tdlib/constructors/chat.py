from ..factory import Method, Type


class chat(Type):
    #  chat. (Can be a private chat, basic group, supergroup, or secret chat)

    id = None  # type: "int53"
    type = None  # type: "ChatType"
    title = None  # type: "string"
    photo = None  # type: "chatPhoto"
    last_message = None  # type: "message"
    order = None  # type: "int64"
    is_pinned = None  # type: "Bool"
    is_marked_as_unread = None  # type: "Bool"
    is_sponsored = None  # type: "Bool"
    can_be_reported = None  # type: "Bool"
    default_disable_notification = None  # type: "Bool"
    unread_count = None  # type: "int32"
    last_read_inbox_message_id = None  # type: "int53"
    last_read_outbox_message_id = None  # type: "int53"
    unread_mention_count = None  # type: "int32"
    notification_settings = None  # type: "chatNotificationSettings"
    reply_markup_message_id = None  # type: "int53"
    draft_message = None  # type: "draftMessage"
    client_data = None  # type: "string"


class getChat(Method):
    #  information about a chat by its identifier, this is
    #  offline request if the current user is not a
    #  @chat_id Chat identifier

    chat_id = None  # type: "int53"


class searchPublicChat(Method):
    #  a public chat by its username. Currently only private
    #  supergroups and channels can be public. Returns the chat
    #  found; otherwise an error is returned @username Username to be resolved

    username = None  # type: "string"


class createPrivateChat(Method):
    #  an existing chat corresponding to a given user @user_id
    #  identifier @force If true, the chat will be created
    #  network request. In this case all information about the
    #  except its type, title and photo can be incorrect

    user_id = None  # type: "int32"
    force = None  # type: "Bool"


class createBasicGroupChat(Method):
    #  an existing chat corresponding to a known basic group
    #  Basic group identifier @force If true, the chat will
    #  created without network request. In this case all information
    #  the chat except its type, title and photo can be incorrect

    basic_group_id = None  # type: "int32"
    force = None  # type: "Bool"


class createSupergroupChat(Method):
    #  an existing chat corresponding to a known supergroup or
    #  @supergroup_id Supergroup or channel identifier @force If true, the
    #  will be created without network request. In this case
    #  information about the chat except its type, title and
    #  can be incorrect

    supergroup_id = None  # type: "int32"
    force = None  # type: "Bool"


class createSecretChat(Method):
    #  an existing chat corresponding to a known secret chat
    #  Secret chat identifier

    secret_chat_id = None  # type: "int32"


class createNewBasicGroupChat(Method):
    #  a new basic group and sends a corresponding messageBasicGroupChatCreate.
    #  the newly created chat @user_ids Identifiers of users to
    #  added to the basic group @title Title of the
    #  basic group; 1-255 characters

    user_ids = None  # type: "vector<int32>"
    title = None  # type: "string"


class createNewSupergroupChat(Method):
    #  a new supergroup or channel and sends a corresponding
    #  Returns the newly created chat @title Title of the
    #  chat; 1-255 characters @is_channel True, if a channel chat
    #  be created @param_description Chat description; 0-255 characters

    title = None  # type: "string"
    is_channel = None  # type: "Bool"
    description = None  # type: "string"


class createNewSecretChat(Method):
    #  a new secret chat. Returns the newly created chat
    #  Identifier of the target user

    user_id = None  # type: "int32"


class upgradeBasicGroupChatToSupergroupChat(Method):
    #  a new supergroup from an existing basic group and
    #  a corresponding messageChatUpgradeTo and messageChatUpgradeFrom. Deactivates the original basic
    #  @chat_id Identifier of the chat to upgrade

    chat_id = None  # type: "int53"


class joinChatByInviteLink(Method):
    #  an invite link to add the current user to
    #  chat if possible. The new member will not be
    #  until the chat state has been synchronized with the

    invite_link = None  # type: "string"
