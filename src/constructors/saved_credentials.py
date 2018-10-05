from tdwrapper.factory import Type


class savedCredentials(Type):
    #  information about saved card credentials @id Unique identifier of
    #  saved credentials @title Title of the saved credentials

    id = None  # type: "string"
    title = None  # type: "string"
