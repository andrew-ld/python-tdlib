from ..factory import Type


class savedCredentials(Type):
    # Contains information about saved card credentials, @id Unique identifier of
    # the saved credentials, @title Title of the saved credentials

    id = None  # type: "string"
    title = None  # type: "string"
