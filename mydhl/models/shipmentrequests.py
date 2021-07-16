from .base import ObjectListModel, BaseModel
from .general import ClientDetail, Request, ServiceHeader

class ShipmentRequest(BaseModel):

    def __init__(self,
        messageid=None,
        clientdetail=None,
        request=None,
        requestedshipment=None
    ):

        self.messageid = messageid
        self.clientdetail = clientdetail if clientdetail else ClientDetail()
        self.request = request if request else Request()
        self.requestedshipment = requestedshipment if requestedshipment else RequestedShipment()