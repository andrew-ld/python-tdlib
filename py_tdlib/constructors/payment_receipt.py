from ..factory import Method, Type


class paymentReceipt(Type):
    # Contains information about a successful payment @date Point in time
    # (Unix timestamp) when the payment was made @payments_provider_user_id User identifier
    # of the payment provider bot @invoice Contains information about the invoice

    date = None  # type: "int32"
    payments_provider_user_id = None  # type: "int32"
    invoice = None  # type: "invoice"
    order_info = None  # type: "orderInfo"
    shipping_option = None  # type: "shippingOption"
    credentials_title = None  # type: "string"


class getPaymentReceipt(Method):
    # Returns information about a successful payment @chat_id Chat identifier of
    # the PaymentSuccessful message @message_id Message identifier

    chat_id = None  # type: "int53"
    message_id = None  # type: "int53"
