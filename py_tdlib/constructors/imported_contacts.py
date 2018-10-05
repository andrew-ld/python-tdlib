from ..factory import Method, Type


class importedContacts(Type):
    # Represents the result of an ImportContacts request @user_ids User identifiers
    # of the imported contacts in the same order as they
    # were specified in the request; 0 if the contact is
    # not yet a registered user

    user_ids = None  # type: "vector<int32>"
    importer_count = None  # type: "vector<int32>"


class importContacts(Method):
    # Adds new contacts or edits existing contacts; contacts' user identifiers
    # are ignored @contacts The list of contacts to import or
    # edit, contact's vCard are ignored and are not imported

    contacts = None  # type: "vector<contact>"


class changeImportedContacts(Method):
    # Changes imported contacts using the list of current user contacts
    # saved on the device. Imports newly added contacts and, if
    # at least the file database is enabled, deletes recently deleted contacts.

    contacts = None  # type: "vector<contact>"
