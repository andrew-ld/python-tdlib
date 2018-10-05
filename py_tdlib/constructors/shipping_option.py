from ..factory import Type


class shippingOption(Type):
    # One shipping option, @id Shipping option identifier, @title Option title
    # @price_parts A list of objects used to calculate the total shipping costs

    id = None  # type: "string"
    title = None  # type: "string"
    price_parts = None  # type: "vector<labeledPricePart>"
