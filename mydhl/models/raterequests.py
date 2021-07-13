from .base import ObjectListModel, BaseModel


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
        totalnet=None,
        charges=None,
        deliverytime=None,
        cutofftime=None,
        nextbusinessdayind=None
    ):

        self.type = type
        self.totalnet = totalnet if totalnet else TotalNet()
        self.charges = charges if charges else Charges()
        self.deliverytime = deliverytime
        self.cutofftime = cutofftime
        self.nextbusinessdayind = nextbusinessdayind

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
        chargecode=None,
        chargetype=None,
        chargeamount=None
    ):

        self.chargecode = chargecode
        self.chargetype = chargetype
        self.chargeamount = chargeamount


class RateRequest(BaseModel):

    def __init__(self,
        clientdetail=None,
        request=None,
        requestedshipment=None
    ):

        self.clientdetail = clientdetail if clientdetail else ClientDetail()
        self.request = request if request else Request()
        self.requestedshipment = requestedshipment if requestedshipment else RequestedShipment()

class ClientDetail(BaseModel):

    def __init__(self,
        so=None,
        plant=None
    ):

        self.so = so
        self.plant = plant

class Request(BaseModel):

    def __init__(self,
        serviceheader=None
    ):

        self.serviceheader = serviceheader if serviceheader else ServiceHeader()

class ServiceHeader(BaseModel):

    def __init__(self,
        messagetime=None,
        messagereference=None,
        webstoreplatform=None,
        webstoreplatformversion=None,
        shippingsystemplatform=None,
        shippingsystemplatformversion=None,
        plugin=None,
        pluginversion=None
    ):

        self.messagetime = messagetime
        self.messagereference = messagereference
        self.webstoreplatform = webstoreplatform
        self.webstoreplatformversion = webstoreplatformversion
        self.shippingsystemplatform = shippingsystemplatform
        self.shippingsystemplatformversion = shippingsystemplatformversion
        self.plugin = plugin
        self.pluginversion = pluginversion

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
        dropofftype=None,
        shiptimestamp=None,
        unitofmeasurement=None,
        content=None,
        paymentinfo=None,
        nextbusinessday=None,
        account=None,
        ship=None,
        packages=None
    ):

        self.dropofftypes = dropofftype
        self.shiptimestamp = shiptimestamp
        self.unitofmeasurement = unitofmeasurement
        self.content = content
        self.paymentinfo = paymentinfo
        self.nextbusinessday = nextbusinessday
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
        streetlines=None,
        streetlines2=None,
        streetlines3=None,
        streetname=None,
        streetnumber=None,
        city=None,
        citydistrict=None,
        stateorprovincecode=None,
        postalcode=None,
        countrycode=None
    ):

        self.streetlines = streetlines
        self.streetlines2 = streetlines2
        self.streetlines3 = streetlines3
        self.streetname = streetname
        self.streetnumber = streetnumber
        self.city = city
        self.citydistrict = citydistrict
        self.stateorprovincecode = stateorprovincecode
        self.postalcode = postalcode
        self.countrycode = countrycode

class Packages(BaseModel):

    def __init__(self,
        requestedpackages=None
    ):
        self.requestedpackages = requestedpackages if requestedpackages else RequestedPackages()


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