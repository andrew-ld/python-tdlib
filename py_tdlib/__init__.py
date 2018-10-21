from .exception import *
from .factory import factorize
from .session import TokenAuth, PhoneAuth
from .wrapper import Client

from gc import get_objects
from signal import signal, SIGINT


def killer(*_):
    for obj in get_objects():
        if isinstance(obj, Client):
            try:
                obj.stop()
            except RpcError as error:
                print(f"[WARNING] {error}")


signal(SIGINT, killer)
