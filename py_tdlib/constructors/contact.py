from ..factory import Type


class contact(Type):
    # Describes a user contact, @phone_number Phone number of the user
    # @first_name First name of the user; 1-255 characters in length
    # @last_name Last name of the user, @vcard Additional data about
    # the user in a form of vCard; 0-2048 bytes in
    # length, @user_id Identifier of the user, if known; otherwise 0

    phone_number = None  # type: "string"
    first_name = None  # type: "string"
    last_name = None  # type: "string"
    vcard = None  # type: "string"
    user_id = None  # type: "int32"
