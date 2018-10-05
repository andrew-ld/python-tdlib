from ..factory import Type


class location(Type):
    #  a location on planet Earth @latitude Latitude of the
    #  in degrees; as defined by the sender @longitude Longitude
    #  the location, in degrees; as defined by the sender

    latitude = None  # type: "double"
    longitude = None  # type: "double"
