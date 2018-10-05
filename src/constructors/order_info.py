from tdwrapper.factory import Method, Type


class orderInfo(Type):
    #  information @name Name of the user @phone_number Phone number
    #  the user @email_address Email address of the user @shipping_address
    #  address for this order; may be null

    name = None  # type: "string"
    phone_number = None  # type: "string"
    email_address = None  # type: "string"
    shipping_address = None  # type: "address"


class getSavedOrderInfo(Method):
    #  saved order info, if any

    pass
