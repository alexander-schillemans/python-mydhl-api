from .base import ObjectListModel, BaseModel

class RateRequest(BaseModel):

    def __init__(self, 
        provider=None
    ):

        self.provider = provider

class Provider(BaseModel):

    def __init__(self,
        code=None,
        notification=None,
        service=None
    ):

        self.code = code
        self.notification = notification if notification else Notification()
        self.service = service if service else Service()

class Notification(BaseModel):
    def __init__(self,
        code=None,
        message=None
    ):

        self.code = code
        self.message = message

class Service(ObjectListModel):

    def __init__(self):

        super(Service, self).init__(list=[])
    

    @property
    def serviceItems(self):
        return self.list

class ServiceItem(BaseModel):

    def __init__(self,
        type=None,
        totalNet=None,
        charges=None,
        deliveryTime=None,
        cutoffTime=None,
        nextBusinessDayInd=None
    ):

        self.type = type
        self.totalNet = totalNet if totalNet else TotalNet()
        self.charges = charges if charges else Charges()
        self.deliveryTime = deliveryTime
        self.cutoffTime = cutoffTime
        self.nextBusinessDayInd = nextBusinessDayInd

class TotalNet(BaseModel):
    
    def __init__(self,
        currency=None,
        amount=None
    ):

        self.currency = currency
        self.amount = amount

class Charges(ObjectListModel):

    def __init__(self,
        currency=None
    ):

        super(Charges, self).init__(list=[])

        self.currency = currency
    
    @property
    def chargeItems(self):
        return self.list

class Charge(BaseModel):

    def __init__(self,
        chargeCode=None,
        chargeType=None,
        chargeAmount=None
    ):

        self.chargeCode = chargeCode
        self.chargeType = chargeType
        self.chargeAmount = chargeAmount