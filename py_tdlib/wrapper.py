from queue import Queue
from . import factorize, Signal
from simplejson import loads, dumps
from threading import Event, Thread
from .constructors import close, error
from .exception import RpcError, RpcTimeout
from ctypes import CDLL, c_char_p, c_void_p, c_double, c_int


class TdJsonClient:
    def __init__(self, td_json: CDLL):
        self.td_create = td_json.td_json_client_create
        self.td_create.restype = c_void_p
        self.td_create.argtypes = []

        self.td_receive = td_json.td_json_client_receive
        self.td_receive.restype = c_char_p
        self.td_receive.argtypes = [c_void_p, c_double]

        self.td_send = td_json.td_json_client_send
        self.td_send.restype = None
        self.td_send.argtypes = [c_void_p, c_char_p]

        self.td_destroy = td_json.td_json_client_destroy
        self.td_destroy.restype = None
        self.td_destroy.argtypes = [c_void_p]

        self.td_verbosity = td_json.td_set_log_verbosity_level
        self.td_verbosity.restype = None
        self.td_verbosity.argtypes = [c_int]

        self.td_execute = td_json.td_json_client_execute
        self.td_execute.restype = c_char_p
        self.td_execute.argtypes = [c_void_p, c_char_p]


class WaitAnswer:
    __answer = RpcTimeout()

    def __init__(self):
        self.__event = Event()

    def wait(self):
        self.__event.wait(3)

    def set_answer(self, update):
        self.__answer = update
        self.__event.set()

    def get_answer(self):
        return self.__answer


class Client(TdJsonClient):
    __offset = 0
    __running = True

    def __init__(self, *args):
        super().__init__(*args)

        self.__waiters = {}
        self.__session = self.td_create()
        Signal.add(self)

        worker = UpdateWorker(self, self.__waiters)
        self.__updates = worker.get_update_queue()
        self.set_verbosity(2)

    def __del__(self):
        self.stop()

    def __get_offset(self) -> int:
        self.__offset += 1
        return self.__offset

    def set_verbosity(self, level: int):
        self.td_verbosity(level)

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
            update = self.td_receive(self.__session, -1)
            yield loads(update)

    def send(self, req):
        offset = self.__get_offset()
        self.__waiters[offset] = WaitAnswer()

        req = req.to_dict()
        req["@extra"] = offset
        req = dumps(req)
        req = req.encode("ascii")

        self.td_send(self.__session, req)
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
