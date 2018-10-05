# python-tdlib

> full oop python 3 tdlib wrapper, fast, thread safe

# install
    python setup.py install

# example
    from ctypes import CDLL
    from py_tdlib import Client, PhoneAuth
    from py_tdlib.constructors import getMe
    
    # demo api key, get your from https://my.telegram.org
    api_id = 94575
    api_hash = "a3406de8d171bb422bb6ddf3bbd800e2"
    
    # creating a client
    tdjson = CDLL("data/tdjson.so")
    client = Client(tdjson)
    
    # login using phone number
    PhoneAuth(api_id, api_hash, client).lets()

    # making an API call
    result = client.send(getMe())
    print(result)

    # get updates
    for update in client.get_updates():
        print(update)
