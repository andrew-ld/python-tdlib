from tdwrapper.factory import Type


class labeledPricePart(Type):
    #  of the price of a product (e.g., "delivery cost",
    #  amount") @label Label for this portion of the product
    #  @amount Currency amount in minimal quantity of the currency

    label = None  # type: "string"
    amount = None  # type: "int53"
