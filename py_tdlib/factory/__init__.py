from .utils import Type, Method, deserialize
from .table import constructors as cs

# monkey patching constructors table

if "__patched" not in cs:
    from .. import constructors

    for k in cs.keys():
        cs[k] = getattr(constructors, k)

    cs["__patched"] = True
