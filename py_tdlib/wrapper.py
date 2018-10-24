from queue import Queue
from .factory import factorize
from simplejson import loads, dumps
from threading import Event, Thread
from .exception import RpcError, RpcTimeout
from .constructors import error, close
from ctypes import CDLL, c_char_p, c_void_p, c_double, c_int


class Pointer:
    def __init__(self, td_json: str):
        td_json = CDLL(td_json)

        self.create = td_json.td_json_client_create
        self.create.restype = c_void_p
        self.create.argtypes = []

        self.receive = td_json.td_json_client_receive
        self.receive.restype = c_char_p
        self.receive.argtypes = [c_void_p, c_double]

        self.send = td_json.td_json_client_send
        self.send.restype = None
        self.send.argtypes = [c_void_p, c_char_p]

        self.destroy = td_json.td_json_client_destroy
        self.destroy.restype = None
        self.destroy.argtypes = [c_void_p]

        self.verbosity = td_json.td_set_log_verbosity_level
        self.verbosity.restype = None
        self.verbosity.argtypes = [c_int]

        self.execute = td_json.td_json_client_execute
        self.execute.restype = c_char_p
        self.execute.argtypes = [c_void_p, c_char_p]


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


class Client:
    __offset = 0
    __running = True

    def __init__(self, pointer: Pointer):
        self.__waiters = {}
        self.__pointer = pointer
        self.__session = self.__pointer.create()

        worker = UpdateWorker(self, self.__waiters)
        self.__updates = worker.get_update_queue()

    @property
    def running(self):
        return self.__running

    def __del__(self):
        self.stop()

    def __get_offset(self) -> int:
        self.__offset += 1
        return self.__offset

    def get_updates(self):
        while self.__running:
            yield self.__updates.get()

    def stop(self, *_):
        if self.__running:
            self.__running = False
            close().run(self, False)

            while not self.__updates.empty():
                self.__updates.get_nowait()

    def receive(self):
        while self.__running:
            update = self.__pointer\
                .receive(self.__session, -1)
            yield loads(update)

    def send(self, req, wait = True):
        offset: int
        req = req.to_dict()

        if wait:
            offset = self.__get_offset()
            self.__waiters[offset] = WaitAnswer()
            req["@extra"] = offset

        req = dumps(req)
        req = req.encode("ascii")

        self.__pointer.send(self.__session, req)

        if not wait:
            return

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
