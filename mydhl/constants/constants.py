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