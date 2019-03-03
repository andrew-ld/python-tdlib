from simplejson import dumps
from .table import constructors as cs


def deserialize(update):
    if isinstance(update, dict):
        c = update.get("@type")
        return cs.get(c, Type)(**update)

    if isinstance(update, list):
        return [*map(deserialize, update)]

    return update


def list_parser(obj):
    result = []

    for x in obj:
        if isinstance(x, list):
            result.append(list_parser(x))

        elif isinstance(x, Obj):
            result.append(x.to_dict())

        else:
            result.append(x)

    return result


class Obj:
    __slots__ = ['__dict__']
    __RESRV = ("@", "_",)

    def to_dict(self):
        result = {"@type": type(self).__name__}

        for k, v in self.__dict__.items():
            if k.startswith(self.__RESRV):
                pass

            elif isinstance(v, Obj):
                result[k] = v.to_dict()

            elif isinstance(v, list):
                result[k] = list_parser(v)

            else:
                result[k] = v

        return result

    def __init__(self, *args, **kwargs):
        args_name = [x for x in vars(type(self)) if not x.startswith(self.__RESRV)]
        self.__dict__ = dict((k, deserialize(v)) for k, v in zip(args_name, args))
        self.__dict__.update(dict((k, deserialize(v)) for k, v in kwargs.items()))

        self.__getattribute__ = self.__dict__.__getitem__
        self.__setattr__ = self.__dict__.__setitem__

    def __len__(self) -> int:
        return len(self.__str__())

    def __repr__(self) -> str:
        result = f"{type(self).__name__}("

        for k, v in self.__dict__.items():
            if not k.startswith(self.__RESRV):
                result += f"{k} = {repr(v)}, "

        if result.endswith(", "):
            return f"{result[:-2]})"

        return f"{result})"

    def __hash__(self) -> int:
        return hash(self.__str__())

    def __str__(self) -> str:
        return dumps(self.to_dict())


class Method(Obj):
    def run(self, client, wait=True):
        return client.send(self, wait)


class Type(Obj):
    pass
