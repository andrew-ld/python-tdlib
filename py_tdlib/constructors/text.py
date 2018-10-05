from ..factory import Method, Type


class text(Type):
    # Contains some text, @text Text

    text = None  # type: "string"


class getFileMimeType(Method):
    # Returns the MIME type of a file, guessed by its
    # extension. Returns an empty string on failure. This is an
    # offline method. Can be called before authorization. Can be called
    # synchronously, @file_name The name of the file or path to the file

    file_name = None  # type: "string"


class getFileExtension(Method):
    # Returns the extension of a file, guessed by its MIME
    # type. Returns an empty string on failure. This is an
    # offline method. Can be called before authorization. Can be called
    # synchronously, @mime_type The MIME type of the file

    mime_type = None  # type: "string"


class cleanFileName(Method):
    # Removes potentially dangerous characters from the name of a file.
    # The encoding of the file name is supposed to be
    # UTF-8. Returns an empty string on failure. This is an
    # offline method. Can be called before authorization. Can be called
    # synchronously, @file_name File name or path to the file

    file_name = None  # type: "string"


class getPreferredCountryLanguage(Method):
    # Returns an IETF language tag of the language preferred in
    # the country, which should be used to fill native fields
    # in Telegram Passport personal details. Returns a 404 error if
    # unknown, @country_code A two-letter ISO 3166-1 alpha-2 country code

    country_code = None  # type: "string"


class getCountryCode(Method):
    # Uses current user IP to found his country. Returns two-letter
    # ISO 3166-1 alpha-2 country code. Can be called before authorization

    pass


class getInviteText(Method):
    # Returns the default text for invitation messages to be used
    # as a placeholder when the current user invites friends to Telegram

    pass


class getProxyLink(Method):
    # Returns an HTTPS link, which can be used to add
    # a proxy. Available only for SOCKS5 and MTProto proxies. Can
    # be called before authorization, @proxy_id Proxy identifier

    proxy_id = None  # type: "int32"
