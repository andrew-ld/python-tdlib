from ..factory import Type


class address(Type):
    # Describes an address @country_code A two-letter ISO 3166-1 alpha-2 country
    # code @state State, if applicable @city City @street_line1 First line
    # of the address @street_line2 Second line of the address @postal_code Address postal code

    country_code = None  # type: "string"
    state = None  # type: "string"
    city = None  # type: "string"
    street_line1 = None  # type: "string"
    street_line2 = None  # type: "string"
    postal_code = None  # type: "string"
