from simplejson import dumps
from .table import constructors


def factorize(update):
    if isinstance(update, dict):
        c = update.get("@type")
        c = constructors.get(c)
        return c(**update)

    if isinstance(update, list):
        return [*map(factorize, update)]

    return update


class Obj:
    def __list_passer(self, obj):
        result = []
        for x in obj:
            if isinstance(x, list):
                result.append(self.__list_passer(x))

            elif hasattr(x, "to_dict"):
                result.append(x.to_dict())

            else:
                result.append(x)

        return result

    def to_dict(self):
        result = {"@type": type(self).__name__}

        for x in vars(self):
            attr = getattr(self, x)

            if hasattr(attr, "to_dict"):
                result[x] = attr.to_dict()

            elif isinstance(attr, list):
                result[x] = self.__list_passer(attr)

            else:
                result[x] = attr

        return result

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            v = factorize(v)
            setattr(self, k, v)

    def __len__(self) -> int:
        return len(self.__str__())

    def __hash__(self):
        return hash(self.__str__())

    def __str__(self) -> str:
        return dumps(self.to_dict())


class Method(Obj):
    def run(self, client):
        return client.send(self)


class Type(Obj):
    pass
