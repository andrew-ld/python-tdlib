from ..factory import Method, Type


class text(Type):
    #  some text @text Text

    text = None  # type: "string"


class getFileMimeType(Method):
    #  the MIME type of a file, guessed by its
    #  Returns an empty string on failure. This is an
    #  method. Can be called before authorization. Can be called
    #  @file_name The name of the file or path to the file

    file_name = None  # type: "string"


class getFileExtension(Method):
    #  the extension of a file, guessed by its MIME
    #  Returns an empty string on failure. This is an
    #  method. Can be called before authorization. Can be called
    #  @mime_type The MIME type of the file

    mime_type = None  # type: "string"


class cleanFileName(Method):
    #  potentially dangerous characters from the name of a file.
    #  encoding of the file name is supposed to be
    #  Returns an empty string on failure. This is an
    #  method. Can be called before authorization. Can be called
    #  @file_name File name or path to the file

    file_name = None  # type: "string"


class getPreferredCountryLanguage(Method):
    #  an IETF language tag of the language preferred in
    #  country, which should be used to fill native fields
    #  Telegram Passport personal details. Returns a 404 error if
    #  @country_code A two-letter ISO 3166-1 alpha-2 country code

    country_code = None  # type: "string"


class getCountryCode(Method):
    #  current user IP to found his country. Returns two-letter
    #  3166-1 alpha-2 country code. Can be called before authorization

    pass


class getInviteText(Method):
    #  the default text for invitation messages to be used
    #  a placeholder when the current user invites friends to

    pass


class getProxyLink(Method):
    #  an HTTPS link, which can be used to add
    #  proxy. Available only for SOCKS5 and MTProto proxies. Can
    #  called before authorization @proxy_id Proxy identifier

    proxy_id = None  # type: "int32"
