from ..factory import Method, Type


class userPrivacySettingRules(Type):
    # A list of privacy rules. Rules are matched in the
    # specified order. The first matched rule defines the privacy setting
    # for a given user. If no rule matches, the action
    # is not allowed, @rules A list of rules

    rules = None  # type: "vector<UserPrivacySettingRule>"


class getUserPrivacySettingRules(Method):
    # Returns the current privacy settings, @setting The privacy setting

    setting = None  # type: "UserPrivacySetting"
