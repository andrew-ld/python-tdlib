from ..factory import Type


class location(Type):
    # Describes a location on planet Earth @latitude Latitude of the
    # location in degrees; as defined by the sender @longitude Longitude
    # of the location, in degrees; as defined by the sender

    latitude = None  # type: "double"
    longitude = None  # type: "double"
