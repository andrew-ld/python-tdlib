from ..factory import Method, Type


class paymentReceipt(Type):
    #  information about a successful payment @date Point in time
    #  timestamp) when the payment was made @payments_provider_user_id User identifier
    #  the payment provider bot @invoice Contains information about the

    date = None  # type: "int32"
    payments_provider_user_id = None  # type: "int32"
    invoice = None  # type: "invoice"
    order_info = None  # type: "orderInfo"
    shipping_option = None  # type: "shippingOption"
    credentials_title = None  # type: "string"


class getPaymentReceipt(Method):
    #  information about a successful payment @chat_id Chat identifier of
    #  PaymentSuccessful message @message_id Message identifier

    chat_id = None  # type: "int53"
    message_id = None  # type: "int53"
