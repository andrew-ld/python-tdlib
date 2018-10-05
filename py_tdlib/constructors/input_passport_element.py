from ..factory import Type


class inputPassportElementPersonalDetails(Type):
    #  Telegram Passport element to be saved containing the user's
    #  details @personal_details Personal details of the user

    personal_details = None  # type: "personalDetails"


class inputPassportElementPassport(Type):
    #  Telegram Passport element to be saved containing the user's
    #  @passport The passport to be saved

    passport = None  # type: "inputIdentityDocument"


class inputPassportElementDriverLicense(Type):
    #  Telegram Passport element to be saved containing the user's
    #  license @driver_license The driver license to be saved

    driver_license = None  # type: "inputIdentityDocument"


class inputPassportElementIdentityCard(Type):
    #  Telegram Passport element to be saved containing the user's
    #  card @identity_card The identity card to be saved

    identity_card = None  # type: "inputIdentityDocument"


class inputPassportElementInternalPassport(Type):
    #  Telegram Passport element to be saved containing the user's
    #  passport @internal_passport The internal passport to be saved

    internal_passport = None  # type: "inputIdentityDocument"


class inputPassportElementAddress(Type):
    #  Telegram Passport element to be saved containing the user's
    #  @address The address to be saved

    address = None  # type: "address"


class inputPassportElementUtilityBill(Type):
    #  Telegram Passport element to be saved containing the user's
    #  bill @utility_bill The utility bill to be saved

    utility_bill = None  # type: "inputPersonalDocument"


class inputPassportElementBankStatement(Type):
    #  Telegram Passport element to be saved containing the user's
    #  statement @bank_statement The bank statement to be saved

    bank_statement = None  # type: "inputPersonalDocument"


class inputPassportElementRentalAgreement(Type):
    #  Telegram Passport element to be saved containing the user's
    #  agreement @rental_agreement The rental agreement to be saved

    rental_agreement = None  # type: "inputPersonalDocument"


class inputPassportElementPassportRegistration(Type):
    #  Telegram Passport element to be saved containing the user's
    #  registration @passport_registration The passport registration page to be saved

    passport_registration = None  # type: "inputPersonalDocument"


class inputPassportElementTemporaryRegistration(Type):
    #  Telegram Passport element to be saved containing the user's
    #  registration @temporary_registration The temporary registration document to be saved

    temporary_registration = None  # type: "inputPersonalDocument"


class inputPassportElementPhoneNumber(Type):
    #  Telegram Passport element to be saved containing the user's
    #  number @phone_number The phone number to be saved

    phone_number = None  # type: "string"


class inputPassportElementEmailAddress(Type):
    #  Telegram Passport element to be saved containing the user's
    #  address @email_address The email address to be saved

    email_address = None  # type: "string"
