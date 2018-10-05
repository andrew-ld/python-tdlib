from ..factory import Method, Type


class orderInfo(Type):
    # Order information @name Name of the user @phone_number Phone number
    # of the user @email_address Email address of the user @shipping_address
    # Shipping address for this order; may be null

    name = None  # type: "string"
    phone_number = None  # type: "string"
    email_address = None  # type: "string"
    shipping_address = None  # type: "address"


class getSavedOrderInfo(Method):
    # Returns saved order info, if any

    pass
