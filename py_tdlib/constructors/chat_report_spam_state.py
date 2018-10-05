from ..factory import Method, Type


class chatReportSpamState(Type):
    #  information about the availability of the "Report spam" action
    #  a chat @can_report_spam True, if a prompt with the
    #  spam" action should be shown to the user

    can_report_spam = None  # type: "Bool"


class getChatReportSpamState(Method):
    #  information on whether the current chat can be reported
    #  spam @chat_id Chat identifier

    chat_id = None  # type: "int53"
