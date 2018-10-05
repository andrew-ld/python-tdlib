from ..factory import Type


class paymentsProviderStripe(Type):
    # Stripe payment provider, @publishable_key Stripe API publishable key, @need_country True,
    # if the user country must be provided, @need_postal_code True, if
    # the user ZIP/postal code must be provided, @need_cardholder_name True, if
    # the cardholder name must be provided

    publishable_key = None  # type: "string"
    need_country = None  # type: "Bool"
    need_postal_code = None  # type: "Bool"
    need_cardholder_name = None  # type: "Bool"
