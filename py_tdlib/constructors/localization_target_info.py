from ..factory import Method, Type


class localizationTargetInfo(Type):
    # Contains information about the current localization target @language_packs List of
    # available language packs for this application

    language_packs = None  # type: "vector<languagePackInfo>"


class getLocalizationTargetInfo(Method):
    # Returns information about the current localization target. This is an
    # offline request if only_local is true @only_local If true, returns
    # only locally available information without sending network requests

    only_local = None  # type: "Bool"
