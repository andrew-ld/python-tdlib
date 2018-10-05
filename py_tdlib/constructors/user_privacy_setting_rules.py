from ..factory import Method, Type


class userPrivacySettingRules(Type):
    #  list of privacy rules. Rules are matched in the
    #  order. The first matched rule defines the privacy setting
    #  a given user. If no rule matches, the action
    #  not allowed @rules A list of rules

    rules = None  # type: "vector<UserPrivacySettingRule>"


class getUserPrivacySettingRules(Method):
    #  the current privacy settings @setting The privacy setting

    setting = None  # type: "UserPrivacySetting"
