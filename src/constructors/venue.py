from ..factory import Type


class venue(Type):
    #  a venue @location Venue location; as defined by the
    #  @title Venue name; as defined by the sender @address
    #  address; as defined by the sender @provider Provider of
    #  venue database; as defined by the sender. Currently only
    #  needs to be supported

    location = None  # type: "location"
    title = None  # type: "string"
    address = None  # type: "string"
    provider = None  # type: "string"
    id = None  # type: "string"
    type = None  # type: "string"
