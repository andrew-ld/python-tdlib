from ..factory import Method, Type


class user(Type):
    #  a user @id User identifier @first_name First name of
    #  user @last_name Last name of the user @username Username of the user

    id = None  # type: "int32"
    first_name = None  # type: "string"
    last_name = None  # type: "string"
    username = None  # type: "string"
    phone_number = None  # type: "string"
    status = None  # type: "UserStatus"
    profile_photo = None  # type: "profilePhoto"
    outgoing_link = None  # type: "LinkState"
    incoming_link = None  # type: "LinkState"
    is_verified = None  # type: "Bool"
    restriction_reason = None  # type: "string"
    have_access = None  # type: "Bool"
    type = None  # type: "UserType"
    language_code = None  # type: "string"


class getMe(Method):
    #  the current user

    pass


class getUser(Method):
    #  information about a user by their identifier. This is
    #  offline request if the current user is not a
    #  @user_id User identifier

    user_id = None  # type: "int32"


class getSupportUser(Method):
    #  a user that can be contacted to get support

    pass
