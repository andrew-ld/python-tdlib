from tdwrapper.factory import Method, Type


class paymentForm(Type):
    #  information about an invoice payment form @invoice Full information
    #  the invoice @url Payment form URL @payments_provider Contains information
    #  the payment provider, if available, to support it natively
    #  the need for opening the URL; may be null

    invoice = None  # type: "invoice"
    url = None  # type: "string"
    payments_provider = None  # type: "paymentsProviderStripe"
    saved_order_info = None  # type: "orderInfo"
    saved_credentials = None  # type: "savedCredentials"
    can_save_credentials = None  # type: "Bool"
    need_password = None  # type: "Bool"


class getPaymentForm(Method):
    #  an invoice payment form. This method should be called
    #  the user presses inlineKeyboardButtonBuy @chat_id Chat identifier of the
    #  message @message_id Message identifier

    chat_id = None  # type: "int53"
    message_id = None  # type: "int53"
