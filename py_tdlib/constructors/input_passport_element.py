from ..factory import Type


class inputPassportElementPersonalDetails(Type):
    # A Telegram Passport element to be saved containing the user's
    # personal details, @personal_details Personal details of the user

    personal_details = None  # type: "personalDetails"


class inputPassportElementPassport(Type):
    # A Telegram Passport element to be saved containing the user's
    # passport, @passport The passport to be saved

    passport = None  # type: "inputIdentityDocument"


class inputPassportElementDriverLicense(Type):
    # A Telegram Passport element to be saved containing the user's
    # driver license, @driver_license The driver license to be saved

    driver_license = None  # type: "inputIdentityDocument"


class inputPassportElementIdentityCard(Type):
    # A Telegram Passport element to be saved containing the user's
    # identity card, @identity_card The identity card to be saved

    identity_card = None  # type: "inputIdentityDocument"


class inputPassportElementInternalPassport(Type):
    # A Telegram Passport element to be saved containing the user's
    # internal passport, @internal_passport The internal passport to be saved

    internal_passport = None  # type: "inputIdentityDocument"


class inputPassportElementAddress(Type):
    # A Telegram Passport element to be saved containing the user's
    # address, @address The address to be saved

    address = None  # type: "address"


class inputPassportElementUtilityBill(Type):
    # A Telegram Passport element to be saved containing the user's
    # utility bill, @utility_bill The utility bill to be saved

    utility_bill = None  # type: "inputPersonalDocument"


class inputPassportElementBankStatement(Type):
    # A Telegram Passport element to be saved containing the user's
    # bank statement, @bank_statement The bank statement to be saved

    bank_statement = None  # type: "inputPersonalDocument"


class inputPassportElementRentalAgreement(Type):
    # A Telegram Passport element to be saved containing the user's
    # rental agreement, @rental_agreement The rental agreement to be saved

    rental_agreement = None  # type: "inputPersonalDocument"


class inputPassportElementPassportRegistration(Type):
    # A Telegram Passport element to be saved containing the user's
    # passport registration, @passport_registration The passport registration page to be saved

    passport_registration = None  # type: "inputPersonalDocument"


class inputPassportElementTemporaryRegistration(Type):
    # A Telegram Passport element to be saved containing the user's
    # temporary registration, @temporary_registration The temporary registration document to be saved

    temporary_registration = None  # type: "inputPersonalDocument"


class inputPassportElementPhoneNumber(Type):
    # A Telegram Passport element to be saved containing the user's
    # phone number, @phone_number The phone number to be saved

    phone_number = None  # type: "string"


class inputPassportElementEmailAddress(Type):
    # A Telegram Passport element to be saved containing the user's
    # email address, @email_address The email address to be saved

    email_address = None  # type: "string"
