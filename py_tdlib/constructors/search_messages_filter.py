from ..factory import Type


class searchMessagesFilterEmpty(Type):
    # Returns all found messages, no filter is applied

    pass


class searchMessagesFilterAnimation(Type):
    # Returns only animation messages

    pass


class searchMessagesFilterAudio(Type):
    # Returns only audio messages

    pass


class searchMessagesFilterDocument(Type):
    # Returns only document messages

    pass


class searchMessagesFilterPhoto(Type):
    # Returns only photo messages

    pass


class searchMessagesFilterVideo(Type):
    # Returns only video messages

    pass


class searchMessagesFilterVoiceNote(Type):
    # Returns only voice note messages

    pass


class searchMessagesFilterPhotoAndVideo(Type):
    # Returns only photo and video messages

    pass


class searchMessagesFilterUrl(Type):
    # Returns only messages containing URLs

    pass


class searchMessagesFilterChatPhoto(Type):
    # Returns only messages containing chat photos

    pass


class searchMessagesFilterCall(Type):
    # Returns only call messages

    pass


class searchMessagesFilterMissedCall(Type):
    # Returns only incoming call messages with missed/declined discard reasons

    pass


class searchMessagesFilterVideoNote(Type):
    # Returns only video note messages

    pass


class searchMessagesFilterVoiceAndVideoNote(Type):
    # Returns only voice and video note messages

    pass


class searchMessagesFilterMention(Type):
    # Returns only messages with mentions of the current user, or
    # messages that are replies to their messages

    pass


class searchMessagesFilterUnreadMention(Type):
    # Returns only messages with unread mentions of the current user
    # or messages that are replies to their messages. When using
    # this filter the results can't be additionally filtered by a
    # query or by the sending user

    pass
