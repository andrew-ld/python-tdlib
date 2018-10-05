from ..factory import Type


class chatReportReasonSpam(Type):
    # The chat contains spam messages

    pass


class chatReportReasonViolence(Type):
    # The chat promotes violence

    pass


class chatReportReasonPornography(Type):
    # The chat contains pornographic messages

    pass


class chatReportReasonCopyright(Type):
    # The chat contains copyrighted content

    pass


class chatReportReasonCustom(Type):
    # A custom reason provided by the user, @text Report text

    text = None  # type: "string"
