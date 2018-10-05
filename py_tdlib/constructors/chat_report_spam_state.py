from ..factory import Method, Type


class chatReportSpamState(Type):
    # Contains information about the availability of the "Report spam" action
    # for a chat, @can_report_spam True, if a prompt with the
    # "Report spam" action should be shown to the user

    can_report_spam = None  # type: "Bool"


class getChatReportSpamState(Method):
    # Returns information on whether the current chat can be reported
    # as spam, @chat_id Chat identifier

    chat_id = None  # type: "int53"
