from ..factory import Type


class chatMembersFilterAdministrators(Type):
    #  the creator and administrators

    pass


class chatMembersFilterMembers(Type):
    #  all chat members, including restricted chat members

    pass


class chatMembersFilterRestricted(Type):
    #  users under certain restrictions in the chat; can be
    #  only by administrators in a supergroup

    pass


class chatMembersFilterBanned(Type):
    #  users banned from the chat; can be used only
    #  administrators in a supergroup or in a channel

    pass


class chatMembersFilterBots(Type):
    #  bot members of the chat

    pass
