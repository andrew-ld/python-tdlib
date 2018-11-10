from sys import hexversion
from werkzeug.utils import secure_filename

from .constructors import (
    setTdlibParameters, tdlibParameters, updateAuthorizationState,
    authorizationStateWaitEncryptionKey, checkDatabaseEncryptionKey,
    getAuthorizationState, authorizationStateWaitPhoneNumber,
    checkAuthenticationBotToken, authorizationStateReady,
    authorizationStateWaitTdlibParameters, setAuthenticationPhoneNumber,
    authorizationStateWaitCode, checkAuthenticationCode,
    authorizationStateWaitPassword, checkAuthenticationPassword,
    updateConnectionState, connectionStateReady
)


class BasicInit:
    def __init__(self, api_id: int, api_hash: str, client, name: str = None):
        self.client = client

        if name:
            directory = "data/sessions/" + secure_filename(name)
        else:
            directory = "data/sessions/default"

        status = getAuthorizationState().run(client)
        assert isinstance(status, authorizationStateWaitTdlibParameters)

        parameters = tdlibParameters(
            use_test_dc = False,
            api_id = api_id,
            api_hash = api_hash,
            database_directory = directory,
            use_chat_info_database = True,
            use_message_database = True,
            enable_storage_optimizer = True,
            system_language_code = "en",
            device_model = "python",
            application_version = "1",
            system_version = str(hexversion),
        )

        setTdlibParameters(parameters = parameters).run(client)


class Auth(BasicInit):
    def token(self, token: str):
        for update in self.client.get_updates():
            if isinstance(update, updateAuthorizationState):
                update = update.authorization_state

            if isinstance(update, updateConnectionState):
                update = update.state

            if isinstance(update, authorizationStateWaitEncryptionKey):
                checkDatabaseEncryptionKey()\
                    .run(self.client)

            elif isinstance(update, authorizationStateWaitPhoneNumber):
                checkAuthenticationBotToken(token = token)\
                    .run(self.client)

            elif isinstance(update, connectionStateReady):
                break

    def phone(self):
        for update in self.client.get_updates():
            if isinstance(update, updateAuthorizationState):
                update = update.authorization_state

            if isinstance(update, authorizationStateWaitEncryptionKey):
                checkDatabaseEncryptionKey()\
                    .run(self.client)

            elif isinstance(update, authorizationStateWaitPhoneNumber):
                req = setAuthenticationPhoneNumber(
                    allow_flash_call = False,
                    is_current_phone_number = False,
                )

                req.phone_number = input("phone: ")
                req.run(self.client)

            elif isinstance(update, authorizationStateWaitCode):
                req = checkAuthenticationCode()
                req.code = input("code: ")

                if not update.is_registered:
                    req.first_name = input("first name: ")
                    req.last_name = input("last name: ")

                req.run(self.client)

            elif isinstance(update, authorizationStateWaitPassword):
                req = checkAuthenticationPassword()
                req.password = input("2step password: ")
                req.run(self.client)

            elif isinstance(update, authorizationStateReady):
                break
