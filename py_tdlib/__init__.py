from .factory import deserialize
from .wrapper import Client, Pointer
from .session import Auth
from .exception import RpcError, RpcTimeout, IllegalRequest

from gc import get_objects
from signal import signal, SIGINT


def killer(*_):
    for obj in get_objects():
        if isinstance(obj, Client):
            obj.stop()


signal(SIGINT, killer)
