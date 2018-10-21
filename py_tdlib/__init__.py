from .factory import factorize
from .wrapper import Client, Pointer
from .session import TokenAuth, PhoneAuth
from .exception import RpcError, RpcTimeout

from gc import get_objects
from signal import signal, SIGINT


def killer(*_):
    for obj in get_objects():
        if isinstance(obj, Client):
            obj.stop()


signal(SIGINT, killer)
