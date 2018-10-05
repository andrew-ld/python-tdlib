from ctypes import CDLL
from tdwrapper import Client, TokenAuth

btoken = input("bot token: ")
tdjson = CDLL("data/tdjson.so")
client = Client(tdjson)

TokenAuth(94575, "a3406de8d171bb422bb6ddf3bbd800e2", client)\
    .lets(btoken)

for update in client.get_updates():
    print(update)
