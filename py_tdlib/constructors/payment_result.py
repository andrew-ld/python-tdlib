from ..factory import Method, Type


class paymentResult(Type):
    # Contains the result of a payment request, @success True, if
    # the payment request was successful; otherwise the verification_url will be
    # not empty, @verification_url URL for additional payment credentials verification

    success = None  # type: "Bool"
    verification_url = None  # type: "string"


class sendPaymentForm(Method):
    # Sends a filled-out payment form to the bot for final
    # verification, @chat_id Chat identifier of the Invoice message, @message_id Message
    # identifier, @order_info_id Identifier returned by ValidateOrderInfo, or an empty string
    # @shipping_option_id Identifier of a chosen shipping option, if applicable

    chat_id = None  # type: "int53"
    message_id = None  # type: "int53"
    order_info_id = None  # type: "string"
    shipping_option_id = None  # type: "string"
    credentials = None  # type: "InputCredentials"
