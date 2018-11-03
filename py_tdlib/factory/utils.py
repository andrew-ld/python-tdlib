from simplejson import dumps
from .table import constructors as cs


def factorize(update):
    if isinstance(update, dict):
        c = update.get("@type")
        return cs.get(c, Type)(**update)

    if isinstance(update, list):
        return [*map(factorize, update)]

    return update


def list_passer(obj):
    result = []

    for x in obj:
        if isinstance(x, list):
            result.append(list_passer(x))

        elif isinstance(x, obj):
            result.append(x.to_dict())

        else:
            result.append(x)

    return result


class Obj:
    def to_dict(self):
        result = {"@type": type(self).__name__}

        for x in vars(self):
            attr = getattr(self, x)

            if isinstance(attr, Obj):
                result[x] = attr.to_dict()

            elif isinstance(attr, list):
                result[x] = list_passer(attr)

            else:
                result[x] = attr

        return result

    def __init__(self, *args, **kwargs):
        pos_args = [x for x in dir(self) if x[0] != "_"]

        if len(args) <= len(pos_args):
            for k, v in zip(pos_args, args):
                v = factorize(v)
                setattr(self, k, v)

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
    def run(self, client, wait = True):
        return client.send(self, wait)


class Type(Obj):
    pass
