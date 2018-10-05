from ..factory import Type


class chatReportReasonSpam(Type):
    #  chat contains spam messages

    pass


class chatReportReasonViolence(Type):
    #  chat promotes violence

    pass


class chatReportReasonPornography(Type):
    #  chat contains pornographic messages

    pass


class chatReportReasonCopyright(Type):
    #  chat contains copyrighted content

    pass


class chatReportReasonCustom(Type):
    #  custom reason provided by the user @text Report text

    text = None  # type: "string"
