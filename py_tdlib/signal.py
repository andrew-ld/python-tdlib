from signal import signal, SIGINT


memory = {
    "started": False,
    "instances": []
}


class Signal:
    @staticmethod
    def add(instance):
        if not memory["started"]:
            signal(SIGINT, Signal.stop)
            memory["started"] = True

        memory["instances"]\
            .append(instance)

    @staticmethod
    def stop(*_):
        clients = memory["instances"]
        for client in clients:
            client.stop()
