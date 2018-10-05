from tdwrapper.factory import Type


class userPrivacySettingRuleAllowAll(Type):
    #  rule to allow all users to do something

    pass


class userPrivacySettingRuleAllowContacts(Type):
    #  rule to allow all of a user's contacts to do something

    pass


class userPrivacySettingRuleAllowUsers(Type):
    #  rule to allow certain specified users to do something
    #  The user identifiers

    user_ids = None  # type: "vector<int32>"


class userPrivacySettingRuleRestrictAll(Type):
    #  rule to restrict all users from doing something

    pass


class userPrivacySettingRuleRestrictContacts(Type):
    #  rule to restrict all contacts of a user from doing something

    pass


class userPrivacySettingRuleRestrictUsers(Type):
    #  rule to restrict all specified users from doing something
    #  The user identifiers

    user_ids = None  # type: "vector<int32>"
