from .utils import Type, Method, deserialize
from .table import constructors as cs
from .. import constructors

# monkey patching constructors table

for k in cs.keys():
    cs[k] = getattr(constructors, k)
