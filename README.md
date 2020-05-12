
## warning: since tdlib memory leak I don't maintain this wrapper anymore because I will never use it again, tell levlam to fix tdlib memory leak, as long as there are these memory leaks over 10gb this mtproto client is a piece of shit

# alternatives which I strongly recommend:

https://docs.pyrogram.org

https://telethon.dev

## python-tdlib

> full oop python 3 tdlib wrapper, fast, thread safe

# install
    sudo pip3 install git+https://github.com/andrew-ld/python-tdlib 

# example
    from py_tdlib import Client, Pointer, Auth
    from py_tdlib.constructors import getMe
    
    # demo api key, get your from https://my.telegram.org
    api_id = 94575
    api_hash = "a3406de8d171bb422bb6ddf3bbd800e2"
    
    # creating a client
    tdjson = Pointer("data/tdjson.so")
    client = Client(tdjson)
    
    # login using phone number
    tdjson.verbosity(0)
    Auth(api_id, api_hash, client).phone()
    
    # login using bot token
    #
    # tdjson.verbosity(0)
    # Auth(api_id, api_hash, client).token("<bot_token>")

    # making an API call
    result = client.send(getMe())
    print(result)

    # get updates
    for update in client.get_updates():
        print(update)

# sending a message
    from py_tdlib.constructors import (
        sendMessage, formattedText
        inputMessageText
    )
    
    result = client.send(
        sendMessage(
            chat_id = <chat_id>,
            input_message_content = inputMessageText(
                text = formattedText(
                    text = "<TEXT>"
                )
            )
        )
    )
