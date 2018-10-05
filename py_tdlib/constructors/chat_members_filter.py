from ..factory import Type


class chatMembersFilterAdministrators(Type):
    # Returns the creator and administrators

    pass


class chatMembersFilterMembers(Type):
    # Returns all chat members, including restricted chat members

    pass


class chatMembersFilterRestricted(Type):
    # Returns users under certain restrictions in the chat; can be
    # used only by administrators in a supergroup

    pass


class chatMembersFilterBanned(Type):
    # Returns users banned from the chat; can be used only
    # by administrators in a supergroup or in a channel

    pass


class chatMembersFilterBots(Type):
    # Returns bot members of the chat

    pass
