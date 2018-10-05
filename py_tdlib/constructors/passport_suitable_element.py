from ..factory import Type


class passportSuitableElement(Type):
    # Contains information about a Telegram Passport element that was requested
    # by a service @type Type of the element @is_selfie_required True,
    # if a selfie is required with the identity document

    type = None  # type: "PassportElementType"
    is_selfie_required = None  # type: "Bool"
    is_translation_required = None  # type: "Bool"
    is_native_name_required = None  # type: "Bool"
