from . import factorize
from queue import Queue
from simplejson import loads, dumps
from threading import Event, Thread
from ctypes import CDLL, c_char_p, c_void_p, c_double, c_int
from .constructors import close, error
from .exception import RpcError, RpcTimeout
from signal import signal, SIGINT


class TdJsonClient:
    def __init__(self, td_json: CDLL):
        self.td_json_client_create = td_json.td_json_client_create
        self.td_json_client_create.restype = c_void_p
        self.td_json_client_create.argtypes = []

        self.td_json_client_receive = td_json.td_json_client_receive
        self.td_json_client_receive.restype = c_char_p
        self.td_json_client_receive.argtypes = [c_void_p, c_double]

        self.td_json_client_send = td_json.td_json_client_send
        self.td_json_client_send.restype = None
        self.td_json_client_send.argtypes = [c_void_p, c_char_p]

        self.td_json_client_destroy = td_json.td_json_client_destroy
        self.td_json_client_destroy.restype = None
        self.td_json_client_destroy.argtypes = [c_void_p]

        self.td_set_log_verbosity_level = td_json.td_set_log_verbosity_level
        self.td_set_log_verbosity_level.restype = None
        self.td_set_log_verbosity_level.argtypes = [c_int]

        self.td_json_client_execute = td_json.td_json_client_execute
        self.td_json_client_execute.restype = c_char_p
        self.td_json_client_execute.argtypes = [c_void_p, c_char_p]

    def td_json_client_create(self) -> int:
        pass

    def td_json_client_receive(self, client: int, timeout: int) -> bytes:
        pass

    def td_json_client_destroy(self, client: int) -> None:
        pass

    def td_set_log_verbosity_level(self, level: int) -> None:
        pass

    def td_json_client_send(self, client: int, req: bytes) -> bytes:
        pass

    def td_json_execute(self, client: int, req: bytes) -> bytes:
        pass


class WaitAnswer:
    __answer = RpcTimeout()

    def __init__(self):
        self.__event = Event()

    def wait(self):
        self.__event.wait(2)

    def set_answer(self, update):
        self.__answer = update
        self.__event.set()

    def get_answer(self):
        return self.__answer


class Client(TdJsonClient):
    __offset = 0
    __running = True

    def __init__(self, *args, **kwargs):
        super(Client, self).__init__(*args, **kwargs)
        self.set_verbosity(0)

        self.__waiters = {}
        self.__session = self.td_json_client_create()

        worker = UpdateWorker(self, self.__waiters)
        self.__updates = worker.get_update_queue()

        signal(SIGINT, self.stop)

    def __del__(self):
        self.stop()

    def __get_offset(self) -> int:
        self.__offset += 1
        return self.__offset

    def set_verbosity(self, level):
        self.td_set_log_verbosity_level(level)

    def get_updates(self):
        while self.__running:
            yield self.__updates.get()

    def stop(self, *_):
        if self.__running:
            close().run(self)
            while not self.__updates.empty():
                self.__updates.get_nowait()

            self.__running = False

    def receive(self):
        while self.__running:
            update = self.td_json_client_receive(self.__session, -1)
            update = loads(update)
            yield update

    def send(self, req):
        offset = self.__get_offset()
        self.__waiters[offset] = WaitAnswer()

        req = req.to_dict()
        req["@extra"] = offset
        req = dumps(req)
        req = req.encode("ascii")

        self.td_json_client_send(self.__session, req)
        self.__waiters[offset].wait()
        res = self.__waiters.pop(offset)\
            .get_answer()

        if isinstance(res, error):
            raise RpcError(res.message)

        if isinstance(res, RpcTimeout):
            raise RpcTimeout()

        return res


class UpdateWorker:
    def __init__(self, client: Client, waiters: dict):
        self.__wrapper = client
        self.__waiters = waiters
        self.__updates = Queue()

        Thread(target = self.__worker).start()

    def get_update_queue(self) -> Queue:
        return self.__updates

    def __worker(self):
        for raw_update in self.__wrapper.receive():
            update = factorize(raw_update)

            if "@extra" not in raw_update:
                self.__updates.put_nowait(update)

            elif raw_update["@extra"] in self.__waiters:
                self.__waiters[raw_update["@extra"]]\
                    .set_answer(update)
