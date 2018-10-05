from tdwrapper.factory import Type


class paymentsProviderStripe(Type):
    #  payment provider @publishable_key Stripe API publishable key @need_country True,
    #  the user country must be provided @need_postal_code True, if
    #  user ZIP/postal code must be provided @need_cardholder_name True, if
    #  cardholder name must be provided

    publishable_key = None  # type: "string"
    need_country = None  # type: "Bool"
    need_postal_code = None  # type: "Bool"
    need_cardholder_name = None  # type: "Bool"
