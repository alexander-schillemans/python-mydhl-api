from .base import ObjectListModel, BaseModel
from .general import ClientDetail, Request, ServiceHeader


class RateResponse(BaseModel):

    def __init__(self, 
        provider=None
    ):

        self.provider = provider if provider else Provider()
    

class Provider(ObjectListModel):

    def __init__(self):

        super(Provider, self).__init__(list=[], listObject=ProviderItem)

    
class ProviderItem(BaseModel):

    def __init__(self,
        code=None,
        notification=None,
        service=None
    ):

        self.code = code
        self.notification = notification if notification else Notification()
        self.service = service if service else Service()


class Notification(ObjectListModel):

    def __init__(self):

        super(Notification, self).__init__(list=[], listObject=NotificationItem)
    

class NotificationItem(BaseModel):
    def __init__(self,
        code=None,
        message=None
    ):

        self.code = code
        self.message = message

class Service(ObjectListModel):

    def __init__(self):

        super(Service, self).__init__(list=[], listObject=ServiceItem)
    
class ServiceItem(BaseModel):

    def __init__(self,
        type=None,
        totalNet=None,
        charges=None,
        deliveryTime=None,
        cutOffTime=None,
        nextBusinessDayInd=None
    ):

        self.type = type
        self.totalNet = totalNet if totalNet else TotalNet()
        self.charges = charges if charges else Charges()
        self.deliveryTime = deliveryTime
        self.cutOffTime = cutOffTime
        self.nextBusinessDayInd = nextBusinessDayInd

class TotalNet(BaseModel):
    
    def __init__(self,
        currency=None,
        amount=None
    ):

        self.currency = currency
        self.amount = amount

class Charges(BaseModel):

    def __init__(self,
        currency=None,
        charge=None
    ):

        self.currency = currency
        self.charge = charge if charge else ChargeList()


class ChargeList(ObjectListModel):

    def __init__(self):

        super(ChargeList, self).__init__(list=[], listObject=Charge)


class Charge(BaseModel):

    def __init__(self,
        chargeCode=None,
        chargeType=None,
        chargeAmount=None
    ):

        self.chargeCode = chargeCode
        self.chargeType = chargeType
        self.chargeAmount = chargeAmount


class RateRequest(BaseModel):

    def __init__(self,
        clientDetail=None,
        request=None,
        requestedShipment=None
    ):

        self.clientDetail = clientDetail if clientDetail else ClientDetail()
        self.request = request if request else Request()
        self.requestedShipment = requestedShipment if requestedShipment else RequestedShipment()

class RequestedShipment(BaseModel):

    REGULAR_PICKUP = 'REGULAR_PICKUP'
    REQUEST_COURIER = 'REQUEST_COURIER'

    MEASUREMENT_SI = 'SI'
    MEASUREMENT_SU = 'SU'

    CONTENT_DOCUMENTS = 'DOCUMENTS'
    CONTENT_NONDOCUMENTS = 'NON_DOCUMENTS'

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

    def __init__(self,
        dropOffType=None,
        shipTimestamp=None,
        unitOfMeasurement=None,
        content=None,
        paymentInfo=None,
        nextBusinessDay=None,
        account=None,
        ship=None,
        packages=None
    ):

        self.dropOffType = dropOffType
        self.shipTimestamp = shipTimestamp
        self.unitOfMeasurement = unitOfMeasurement
        self.content = content
        self.paymentInfo = paymentInfo
        self.nextBusinessDay = nextBusinessDay
        self.account = account,
        self.ship = ship if ship else Ship()
        self.packages = packages if packages else Packages()

class Ship(BaseModel):

    def __init__(self,
        shipper=None,
        recipient=None
    ):

        self.shipper = shipper if shipper else PersonalInfo()
        self.recipient = recipient if recipient else PersonalInfo()


class PersonalInfo(BaseModel):

    def __init__(self,
        streetLines=None,
        streetLines2=None,
        streetLines3=None,
        streetName=None,
        streetNumber=None,
        city=None,
        cityDistrict=None,
        stateOrProvinceCode=None,
        postalCode=None,
        countryCode=None
    ):

        self.streetLines = streetLines
        self.streetLines2 = streetLines2
        self.streetLines3 = streetLines3
        self.streetName = streetName
        self.streetNumber = streetNumber
        self.city = city
        self.cityDistrict = cityDistrict
        self.stateOrProvinceCode = stateOrProvinceCode
        self.postalCode = postalCode
        self.countryCode = countryCode

class Packages(BaseModel):

    def __init__(self,
        requestedPackages=None
    ):
        self.requestedPackages = requestedPackages if requestedPackages else RequestedPackages()


class RequestedPackages(ObjectListModel):

    def __init__(self):
        super(RequestedPackages, self).__init__(list=[], listObject=RequestedPackage)
    

class RequestedPackage(BaseModel):

    def __init__(self,
        number=None,
        weight=None,
        dimensions=None
    ):

        self.number = number
        self.weight = weight if weight else Weight()
        self.dimensions = dimensions if dimensions else Dimensions()

class Weight(BaseModel):

    def __init__(self,
        value=None
    ):

        self.value = value

class Dimensions(BaseModel):

    def __init__(self,
        length=None,
        width=None,
        height=None
    ):

        self.length = length
        self.width = width
        self.height = height