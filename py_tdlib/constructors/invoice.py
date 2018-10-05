from ..factory import Type


class invoice(Type):
    #  invoice @currency ISO 4217 currency code @price_parts A list
    #  objects used to calculate the total price of the
    #  @is_test True, if the payment is a test payment

    currency = None  # type: "string"
    price_parts = None  # type: "vector<labeledPricePart>"
    is_test = None  # type: "Bool"
    need_name = None  # type: "Bool"
    need_phone_number = None  # type: "Bool"
    need_email_address = None  # type: "Bool"
    need_shipping_address = None  # type: "Bool"
    send_phone_number_to_provider = None  # type: "Bool"
    send_email_address_to_provider = None  # type: "Bool"
    is_flexible = None  # type: "Bool"
