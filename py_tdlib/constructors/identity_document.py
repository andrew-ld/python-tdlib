from ..factory import Type


class identityDocument(Type):
    # An identity document, @number Document number; 1-24 characters, @expiry_date Document
    # expiry date; may be null, @front_side Front side of the document

    number = None  # type: "string"
    expiry_date = None  # type: "date"
    front_side = None  # type: "datedFile"
    reverse_side = None  # type: "datedFile"
    selfie = None  # type: "datedFile"
    translation = None  # type: "vector<datedFile>"
