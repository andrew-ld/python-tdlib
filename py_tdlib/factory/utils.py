from simplejson import dumps
from .table import constructors as cs


def deserialize(update):
    if isinstance(update, dict):
        c = update.get("@type")
        return cs.get(c, Type)(**update)

    if isinstance(update, list):
        return [*map(deserialize, update)]

    return update


def list_passer(obj):
    result = []

    for x in obj:
        if isinstance(x, list):
            result.append(list_passer(x))

        elif isinstance(x, Obj):
            result.append(x.to_dict())

        else:
            result.append(x)

    return result


class Obj:
    def to_dict(self):
        result = {"@type": type(self).__name__}

        for k, v in self.__dict__.items():
            if k.startswith("_"):
                pass

            elif isinstance(v, Obj):
                result[k] = v.to_dict()

            elif isinstance(v, list):
                result[k] = list_passer(v)

            else:
                result[k] = v

        return result

    def __init__(self, *args, **kwargs):
        args_name = [x for x in vars(type(self)) if x[0] != "_"]

        self.__dict__ = dict((k, deserialize(v)) for k, v in zip(args_name, args))
        self.__dict__.update(dict((k, deserialize(v)) for k, v in kwargs.items()))

        self.__getattribute__ = self.__dict__.__getitem__
        self.__setattr__ = self.__dict__.__setitem__

    def __len__(self) -> int:
        return len(self.__str__())

    def __hash__(self):
        return hash(self.__str__())

    def __str__(self) -> str:
        return dumps(self.to_dict())


class Method(Obj):
    def run(self, client, wait=True):
        return client.send(self, wait)


class Type(Obj):
    pass
