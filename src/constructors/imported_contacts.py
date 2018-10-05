from tdwrapper.factory import Method, Type


class importedContacts(Type):
    #  the result of an ImportContacts request @user_ids User identifiers
    #  the imported contacts in the same order as they
    #  specified in the request; 0 if the contact is
    #  yet a registered user

    user_ids = None  # type: "vector<int32>"
    importer_count = None  # type: "vector<int32>"


class importContacts(Method):
    #  new contacts or edits existing contacts; contacts' user identifiers
    #  ignored @contacts The list of contacts to import or
    #  contact's vCard are ignored and are not imported

    contacts = None  # type: "vector<contact>"


class changeImportedContacts(Method):
    #  imported contacts using the list of current user contacts
    #  on the device. Imports newly added contacts and, if
    #  least the file database is enabled, deletes recently deleted

    contacts = None  # type: "vector<contact>"
