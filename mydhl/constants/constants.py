class DropOffType:
    REGULAR_PICKUP = 'REGULAR_PICKUP'
    REQUEST_COURIER = 'REQUEST_COURIER'

class PaymentInfo:
    PAYMENT_CFR = 'CFR'
    PAYMENT_CIF = 'CIF'
    PAYMENT_CIP = 'CIP'
    PAYMENT_CPT = 'CPT'
    PAYMENT_DAF = 'DAF'
    PAYMENT_DDP = 'DPP'
    PAYMENT_DDU = 'DDU'
    PAYMENT_DAP = 'DAP'
    PAYMENT_DEQ = 'DEQ'
    PAYMENT_DES = 'DES'
    PAYMENT_EXW = 'EXW'
    PAYMENT_FAS = 'FAS'
    PAYMENT_FCA = 'FCA'
    PAYMENT_FOB = 'FOB'

class ContentType:
    DOCUMENTS = 'DOCUMENTS'
    NON_DOCUMENTS = 'NON_DOCUMENTS'

class Measurement:
    MEASUREMENT_METRIC = 'SI'
    MEASUREMENT_US = 'SU'

class OnDemandDelivery:
    SERVICE_POINT = 'TV'
    LEAVE_AT_NEIGHBOUR = 'SW'
    SIGNATURE_NEEDED = 'SX'

class RegistrationNumberType:
    VAT = 'VAT'
    EIN = 'EIN'
    GST = 'GST'
    SSN = 'SSN'
    EOR = 'EOR'
    DUN = 'DUN'
    FED = 'FED'
    STA = 'STA'
    CNP = 'CNP'
    IE = 'IE'
    INN = 'INN'
    KPP = 'KPP'
    OGR = 'OGR'
    OKP = 'OKP'
    MRN = 'MRN'
    OSR = 'OSR'

class NotificationMethods:
    EMAIL = 'EMAIL'

PRODUCTS = {

    'TDK' : 'Express 9:00 - Documents',
    'K' : 'Express 9:00 - Documents',

    'TDE' : 'Express 9:00 - NonDocuments',
    'C' : 'Express 9:00 - NonDocuments',
    'E' : 'Express 9:00 - NonDocuments',

    'TDL' : 'Express 10:30',
    'J' : 'Express 10:30 - Documents',
    'L' : 'Express 10:30 - Documents',

    'X' : 'Express 10:30 - NonDocuments',
    'M' : 'Express 10:30 - NonDocuments',

    'TDT' : 'Express 12:00 - Documents',
    'T' : 'Express 12:00 - Documents',

    'TDY' : 'Express 12:00 - NonDocuments',
    'Y' : 'Express 12:00 - NonDocuments',

    'ECX' : 'Express Worldwide',
    'U' : 'Express Worldwide',

    'DOX' : 'Express Worldwide - Documents',
    'D' : 'Express Worldwide - Documents',

    'WPX' : 'Express Worldwide - NonDocuments',
    'S' : 'Express Worldwide - NonDocuments',
    'P' : 'Express Worldwide - NonDocuments',

    'DOK' : 'Express 9:00 - Domestic',
    '7' : 'Express 9:00 - Domestic',
    'I' : 'Express 9:00 - Domestic',
    
    'DOT' : 'Express 12:00 - Domestic',
    '8' : 'Express 12:00 - Domestic',
    '1' : 'Express 12:00 - Domestic',

    'DOM' : 'Express 18:00 - Domestic',
    'L' : 'Express 18:00 - Domestic',
    'N' : 'Express 18:00 - Domestic',

    'ESU' : 'Economy Select - Documents',
    'W' : 'Economy Select - Documents',

    'ESI' : 'Economy Select - NonDocuments',
    'H' : 'Economy Select - NonDocuments',

    'XPD' : 'Express Enveloppe - Documents under 0.3kg',
    'E' : 'Express Enveloppe - Documents under 0.3kg',
    # 'X' : 'Express Enveloppe - Documents under 0.3kg',


}