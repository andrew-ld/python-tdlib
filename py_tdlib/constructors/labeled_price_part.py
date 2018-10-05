from ..factory import Type


class labeledPricePart(Type):
    # Portion of the price of a product (e.g., "delivery cost",
    # "tax amount") @label Label for this portion of the product
    # price @amount Currency amount in minimal quantity of the currency

    label = None  # type: "string"
    amount = None  # type: "int53"
