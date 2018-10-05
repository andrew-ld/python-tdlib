from ..factory import Method, Type


class chatMembers(Type):
    #  a list of chat members @total_count Approximate total count
    #  chat members found @members A list of chat members

    total_count = None  # type: "int32"
    members = None  # type: "vector<chatMember>"


class searchChatMembers(Method):
    #  for a specified query in the first name, last
    #  and username of the members of a specified chat.
    #  administrator rights in channels @chat_id Chat identifier @query Query
    #  search for @limit The maximum number of users to
    #  returned @filter The type of users to return. By default, chatMembersFilterMembers

    chat_id = None  # type: "int53"
    query = None  # type: "string"
    limit = None  # type: "int32"
    filter = None  # type: "ChatMembersFilter"


class getSupergroupMembers(Method):
    #  information about members or banned users in a supergroup
    #  channel. Can be used only if SupergroupFullInfo.can_get_members == true;
    #  administrator privileges may be required for some filters @supergroup_id
    #  of the supergroup or channel

    supergroup_id = None  # type: "int32"
    filter = None  # type: "SupergroupMembersFilter"
    offset = None  # type: "int32"
    limit = None  # type: "int32"
