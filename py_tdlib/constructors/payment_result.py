from ..factory import Method, Type


class paymentResult(Type):
    #  the result of a payment request @success True, if
    #  payment request was successful; otherwise the verification_url will be
    #  empty @verification_url URL for additional payment credentials verification

    success = None  # type: "Bool"
    verification_url = None  # type: "string"


class sendPaymentForm(Method):
    #  a filled-out payment form to the bot for final
    #  @chat_id Chat identifier of the Invoice message @message_id Message
    #  @order_info_id Identifier returned by ValidateOrderInfo, or an empty string
    #  Identifier of a chosen shipping option, if applicable

    chat_id = None  # type: "int53"
    message_id = None  # type: "int53"
    order_info_id = None  # type: "string"
    shipping_option_id = None  # type: "string"
    credentials = None  # type: "InputCredentials"
