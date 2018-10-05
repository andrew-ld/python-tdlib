from tdwrapper.factory import Type


class searchMessagesFilterEmpty(Type):
    #  all found messages, no filter is applied

    pass


class searchMessagesFilterAnimation(Type):
    #  only animation messages

    pass


class searchMessagesFilterAudio(Type):
    #  only audio messages

    pass


class searchMessagesFilterDocument(Type):
    #  only document messages

    pass


class searchMessagesFilterPhoto(Type):
    #  only photo messages

    pass


class searchMessagesFilterVideo(Type):
    #  only video messages

    pass


class searchMessagesFilterVoiceNote(Type):
    #  only voice note messages

    pass


class searchMessagesFilterPhotoAndVideo(Type):
    #  only photo and video messages

    pass


class searchMessagesFilterUrl(Type):
    #  only messages containing URLs

    pass


class searchMessagesFilterChatPhoto(Type):
    #  only messages containing chat photos

    pass


class searchMessagesFilterCall(Type):
    #  only call messages

    pass


class searchMessagesFilterMissedCall(Type):
    #  only incoming call messages with missed/declined discard reasons

    pass


class searchMessagesFilterVideoNote(Type):
    #  only video note messages

    pass


class searchMessagesFilterVoiceAndVideoNote(Type):
    #  only voice and video note messages

    pass


class searchMessagesFilterMention(Type):
    #  only messages with mentions of the current user, or
    #  that are replies to their messages

    pass


class searchMessagesFilterUnreadMention(Type):
    #  only messages with unread mentions of the current user
    #  messages that are replies to their messages. When using
    #  filter the results can't be additionally filtered by a
    #  or by the sending user

    pass
