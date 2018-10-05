from ..factory import Method, Type


class localizationTargetInfo(Type):
    #  information about the current localization target @language_packs List of
    #  language packs for this application

    language_packs = None  # type: "vector<languagePackInfo>"


class getLocalizationTargetInfo(Method):
    #  information about the current localization target. This is an
    #  request if only_local is true @only_local If true, returns
    #  locally available information without sending network requests

    only_local = None  # type: "Bool"
