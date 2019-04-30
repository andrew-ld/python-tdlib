from ..factory import Type


class pageBlockRelatedArticles(Type):
	header = None  # type: "RichText"
	articles = None  # type: "vector<pageBlockRelatedArticle>"
