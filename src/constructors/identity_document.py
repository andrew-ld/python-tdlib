from tdwrapper.factory import Type


class identityDocument(Type):
    #  identity document @number Document number; 1-24 characters @expiry_date Document
    #  date; may be null @front_side Front side of the

    number = None  # type: "string"
    expiry_date = None  # type: "date"
    front_side = None  # type: "datedFile"
    reverse_side = None  # type: "datedFile"
    selfie = None  # type: "datedFile"
    translation = None  # type: "vector<datedFile>"
