from tdwrapper.factory import Method, Type


class validatedOrderInfo(Type):
    #  a temporary identifier of validated order information, which is
    #  for one hour. Also contains the available shipping options
    #  Temporary identifier of the order information @shipping_options Available shipping

    order_info_id = None  # type: "string"
    shipping_options = None  # type: "vector<shippingOption>"


class validateOrderInfo(Method):
    #  the order information provided by a user and returns
    #  available shipping options for a flexible invoice @chat_id Chat
    #  of the Invoice message @message_id Message identifier @order_info The
    #  information, provided by the user @allow_save True, if the
    #  information can be saved

    chat_id = None  # type: "int53"
    message_id = None  # type: "int53"
    order_info = None  # type: "orderInfo"
    allow_save = None  # type: "Bool"
