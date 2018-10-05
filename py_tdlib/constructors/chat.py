from ..factory import Method, Type


class chat(Type):
    # A chat. (Can be a private chat, basic group, supergroup, or secret chat)

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
    # Returns information about a chat by its identifier, this is
    # an offline request if the current user is not a
    # bot @chat_id Chat identifier

    chat_id = None  # type: "int53"


class searchPublicChat(Method):
    # Searches a public chat by its username. Currently only private
    # chats, supergroups and channels can be public. Returns the chat
    # if found; otherwise an error is returned @username Username to be resolved

    username = None  # type: "string"


class createPrivateChat(Method):
    # Returns an existing chat corresponding to a given user @user_id
    # User identifier @force If true, the chat will be created
    # without network request. In this case all information about the
    # chat except its type, title and photo can be incorrect

    user_id = None  # type: "int32"
    force = None  # type: "Bool"


class createBasicGroupChat(Method):
    # Returns an existing chat corresponding to a known basic group
    # @basic_group_id Basic group identifier @force If true, the chat will
    # be created without network request. In this case all information
    # about the chat except its type, title and photo can be incorrect

    basic_group_id = None  # type: "int32"
    force = None  # type: "Bool"


class createSupergroupChat(Method):
    # Returns an existing chat corresponding to a known supergroup or
    # channel @supergroup_id Supergroup or channel identifier @force If true, the
    # chat will be created without network request. In this case
    # all information about the chat except its type, title and
    # photo can be incorrect

    supergroup_id = None  # type: "int32"
    force = None  # type: "Bool"


class createSecretChat(Method):
    # Returns an existing chat corresponding to a known secret chat
    # @secret_chat_id Secret chat identifier

    secret_chat_id = None  # type: "int32"


class createNewBasicGroupChat(Method):
    # Creates a new basic group and sends a corresponding messageBasicGroupChatCreate.
    # Returns the newly created chat @user_ids Identifiers of users to
    # be added to the basic group @title Title of the
    # new basic group; 1-255 characters

    user_ids = None  # type: "vector<int32>"
    title = None  # type: "string"


class createNewSupergroupChat(Method):
    # Creates a new supergroup or channel and sends a corresponding
    # messageSupergroupChatCreate. Returns the newly created chat @title Title of the
    # new chat; 1-255 characters @is_channel True, if a channel chat
    # should be created @param_description Chat description; 0-255 characters

    title = None  # type: "string"
    is_channel = None  # type: "Bool"
    description = None  # type: "string"


class createNewSecretChat(Method):
    # Creates a new secret chat. Returns the newly created chat
    # @user_id Identifier of the target user

    user_id = None  # type: "int32"


class upgradeBasicGroupChatToSupergroupChat(Method):
    # Creates a new supergroup from an existing basic group and
    # sends a corresponding messageChatUpgradeTo and messageChatUpgradeFrom. Deactivates the original basic
    # group @chat_id Identifier of the chat to upgrade

    chat_id = None  # type: "int53"


class joinChatByInviteLink(Method):
    # Uses an invite link to add the current user to
    # the chat if possible. The new member will not be
    # added until the chat state has been synchronized with the server

    invite_link = None  # type: "string"
