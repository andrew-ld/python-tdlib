from ..factory import Method, Type


class validatedOrderInfo(Type):
    # Contains a temporary identifier of validated order information, which is
    # stored for one hour. Also contains the available shipping options
    # @order_info_id Temporary identifier of the order information @shipping_options Available shipping options

    order_info_id = None  # type: "string"
    shipping_options = None  # type: "vector<shippingOption>"


class validateOrderInfo(Method):
    # Validates the order information provided by a user and returns
    # the available shipping options for a flexible invoice @chat_id Chat
    # identifier of the Invoice message @message_id Message identifier @order_info The
    # order information, provided by the user @allow_save True, if the
    # order information can be saved

    chat_id = None  # type: "int53"
    message_id = None  # type: "int53"
    order_info = None  # type: "orderInfo"
    allow_save = None  # type: "Bool"
