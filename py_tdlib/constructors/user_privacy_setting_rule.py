from ..factory import Type


class userPrivacySettingRuleAllowAll(Type):
    # A rule to allow all users to do something

    pass


class userPrivacySettingRuleAllowContacts(Type):
    # A rule to allow all of a user's contacts to do something

    pass


class userPrivacySettingRuleAllowUsers(Type):
    # A rule to allow certain specified users to do something
    # @user_ids The user identifiers

    user_ids = None  # type: "vector<int32>"


class userPrivacySettingRuleRestrictAll(Type):
    # A rule to restrict all users from doing something

    pass


class userPrivacySettingRuleRestrictContacts(Type):
    # A rule to restrict all contacts of a user from doing something

    pass


class userPrivacySettingRuleRestrictUsers(Type):
    # A rule to restrict all specified users from doing something
    # @user_ids The user identifiers

    user_ids = None  # type: "vector<int32>"
