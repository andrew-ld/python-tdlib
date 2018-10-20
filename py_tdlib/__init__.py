from .exception import *
from .factory import factorize
from signal import signal, SIGINT
from .session import TokenAuth, PhoneAuth
from .wrapper import Client

if "__tdlib_k" not in globals():
    globals()["__tdlib_s"] = []
    globals()["__tdlib_k"] = True

    def killer():
        for client in globals()["__tdlib_s"]:
            if isinstance(client, Client):
                client.stop()

    signal(SIGINT, killer)
